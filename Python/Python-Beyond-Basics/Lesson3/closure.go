package main

import (
	"fmt"
)

var count = 1

func main() {
	fmt.Println(count)
	lf := enclosing()
	fmt.Println(lf())
	fmt.Println(lf())
	fmt.Println(lf())
}

func enclosing() func() int {
	count := 1
	return func() int {
		count++
		return count
	}
}
