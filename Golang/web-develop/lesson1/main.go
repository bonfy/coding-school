package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

// Handler
type hiHandler struct{}

func (h *hiHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hi, world!"))
}

// HandlerFunc
func helloHandler(w http.ResponseWriter, req *http.Request) {
	io.WriteString(w, "hello, world!\n")
}

func main() {

	// 方法一: Handler 实现
	http.Handle("/hi", &hiHandler{})

	// 方法二: 通过 HandlerFunc 把函数转换成 Handler 接口的实现对象
	hh := http.HandlerFunc(helloHandler)
	http.Handle("/hello", hh)

	// 方法三: 直接使用 HandleFunc
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello Go!"))
	})

	port := ":8080"
	fmt.Printf("Server Listen in http://localhost%s\n", port)
	log.Fatal(http.ListenAndServe(port, nil))
}
