# Template Built-in

## Functions

* template
* define
* block
* html
* js
* urlquery
* index
* print/printf/println
* len
* with


## Custom Functions

pipeline:
* Func return a single value
* Func return a single value and an error type

```go
template.Func(funcMap FuncMap) *Template

type FuncMap map[string]interface{}

template.New("").Funcs(funcMap).Parse(...)
```