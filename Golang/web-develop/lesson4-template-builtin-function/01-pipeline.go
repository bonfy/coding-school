package main

import (
	"html/template"
	"os"
)

const tax = 6.75 / 100

type Product struct {
	Name  string
	Price float32
}

func (p Product) PriceWithTax() float32 {
	return p.Price * (1 + tax)
}

const templateString = `
{{- "Item Information" }}
Name: {{ .Name }}
Price: {{ .Price |  printf "$%.2f" }}
Price with Tax: {{ .PriceWithTax | printf "$%.2f" }}
`

func main() {
	p := Product{
		Name:  "Lemonade",
		Price: 2.16,
	}
	t := template.Must(template.New("").Parse(templateString))
	t.Execute(os.Stdout, p)
}
