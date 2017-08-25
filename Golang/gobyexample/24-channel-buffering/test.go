package main

import (
	"time"
	"fmt"
)

func main() {
	messages := make(chan string, 5)

	go func () {
		for i:=0; i < 5; i++ {
			time.Sleep(time.Second)
			fmt.Println("[Channel 1] send", i)
			messages <- fmt.Sprintf("[Message] channel 1 - %d", i)
		}
	}()

	go func () {
		for i:=0; i < 4; i++ {
			time.Sleep(2*time.Second)
			fmt.Println("[Channel 2] send", i)
			messages <- fmt.Sprintf("[Message] channel 2 - %d", i)
		}
	}()

	for true {
		msg := <- messages
		fmt.Println("[Recieve]", msg)
	}
}
