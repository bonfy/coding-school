package main

import (
	"fmt"
	"html/template"
	"os"
)

// User Model
type User struct {
	Name string
	Age  int
}

func main() {
	templateStr := `Hello {{.Name}}`
	t, err := template.New("title").Parse(templateStr)
	if err != nil {
		fmt.Println(err)
	}

	err = t.Execute(os.Stdout, &User{Name: "Jack"})
	if err != nil {
		fmt.Println(err)
	}
}
