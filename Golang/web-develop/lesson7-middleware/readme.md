# MiddleWare

## What is middleware

request  -> middleware -> RequestHandler
response <- middleware <- RequestHandler

## Creating middleware

```go
http.ListenAndServe(addr string, handler Handler) error

type Handler interface {
    serveHTTP(ResponseWriter, *Request)
}

type MyMiddleware struct {
    Next http.Handler
}

func (m MyMiddleware) ServeHTTP(w http.ResponseWriter, r *http.Request){
    // do something before next handler

    m.Next.ServeHTTP(w, r)

    // do something after next handler
}
```

## Usage

* Logging
* Security
* Request Timeouts
* Response compression

## Request Context

```go

func (*Request) Context() context.Context

func (*Request) WithContext(ctx context.Context) context.Context

// Context

type Context interface {
    Deadline() (deadline time.Time, ok bool)
    Done() <-chan struct{}
    Err() error
    Value(key interface{}) interface{}
}
```

gzip.go
```go
package middleware

import (
	"compress/gzip"
	"io"
	"net/http"
	"strings"
)

type GzipMiddleware struct {
	Next http.Handler
}

func (gm *GzipMiddleware) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if gm.Next == nil {
		gm.Next = http.DefaultServeMux
	}

	encodings := r.Header.Get("Accept-Encoding")
	if !strings.Contains(encodings, "gzip") {
		gm.Next.ServeHTTP(w, r)
		return
	}
	w.Header().Add("Content-Encoding", "gzip")
	gzipWriter := gzip.NewWriter(w)
	defer gzipWriter.Close()
	grw := gzipResponseWriter{
		ResponseWriter: w,
		Writer:         gzipWriter,
	}
	gm.Next.ServeHTTP(grw, r)
}

type gzipResponseWriter struct {
	http.ResponseWriter
	io.Writer
}

func (grw gzipResponseWriter) Write(data []byte) (int, error) {
	return grw.Writer.Write(data)
}

```

timeout.go
```go
package middleware

import (
	"context"
	"net/http"
	"time"
)

type TimeoutMiddleware struct {
	Next http.Handler
}

func (tm TimeoutMiddleware) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if tm.Next == nil {
		tm.Next = http.DefaultServeMux
	}

	ctx := r.Context()
	ctx, _ = context.WithTimeout(ctx, 3*time.Second)
	r.WithContext(ctx)
	ch := make(chan struct{})
	go func() {
		tm.Next.ServeHTTP(w, r)
		ch <- struct{}{}
	}()
	select {
	case <-ch:
		return
	case <-ctx.Done():
		w.WriteHeader(http.StatusRequestTimeout)
	}

}
```

```go
http.ListenAndServe(":8000", &middleware.TimeoutMiddleware{new(middleware.GzipMiddleware)})
```