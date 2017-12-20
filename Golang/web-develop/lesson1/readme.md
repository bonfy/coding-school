# Basic

## 参考

> [http://cizixs.com/2016/08/17/golang-http-server-side](http://cizixs.com/2016/08/17/golang-http-server-side)
> [web基础](https://github.com/astaxie/build-web-application-with-golang/blob/master/zh/03.0.md)

## HTTP 

1. Handling Connection -> Go http.DefaultServeMux
2. Handling Request
```go
// http.Handle

func Handle(pattern string, handler Handler)

type Handle interface {
    ServeHTTP(ResponseWriter, *Request)
}

// http.HandleFunc

func HandleFunc(pattern string, handler HandlerFunc)

type HandlerFunc func(ResponseWriter, *Request)

func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request) {
	f(w, r)
}
```

```go
// 第一种 不设置 handler

http.ListenAndServe(":8888", nil)

// 第二种 新建 mux(多路复用器) , handler -> mux 

mux := http.NewServeMux()
mux.HandleFunc("/", echoHandler)
http.ListenAndServe(":8888", mux)

// 第三种 内置的 handler

http.ListenAndServe(":8888", http.FileServer(http.Dir(".")))
```

## Built-in Handler

* NotFoundHandler
* RedirectHandler
* StripPrefix
* TimeoutHandler
* FileServer