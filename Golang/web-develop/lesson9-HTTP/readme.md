# HTTP

## HTTP vs HTTPS

HTTPS 加了一层  TLS

```go
// HTTP
http.ListenAndServe

// HTTPS
http.ListenAndServeTLS
```

下载 crypto/tls/generate_cert.go

```cmd
go run generate_cert.go -h

go run generate_cert.go -host localhost
```


## HTTP2

慎用 server push, 因为客户端缓存会失效, 毕竟如果有缓存，就不用再加载了，推也是需要时间的

所以 server push 在视频推流肯定是有用的

