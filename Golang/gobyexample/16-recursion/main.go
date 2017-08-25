package main

import "fmt"

func fact(n int) int {
	if n==0 {
		return 1
	}
	fmt.Println(n, "*fact(", n-1, ")")
	return n * fact(n-1)
}

func main() {
	result := fact(7)
	fmt.Println(result)
}
