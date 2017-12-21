# HTTP Requests

## Query pramameters

如: https://localhost:8000/search?q=products&page=1 

q=products&page=1 

```go
url := r.URL            // net/url.URL
query := url.Query()    // Values (map[string][]string)
q := query["q"]         // []string{“products”}
page := query.Get("page")// "1"
```

## Form data

```go
err := r.ParseForm() // populate Form and PostForm
f := r.Form // net/url.Values
username := f["username"] // []string {"mike"}
pass := f.Get("password") // "password1"
```


## Json

### Read Json

```go

type Query struct { 
    Term     string `json:"term"`
    Page     int    `json:"page"`
    PageSize int    `json:"pageSize"`
}

func (w http.ResponseWriter, r *http.Request) {
    dec := json.NewDecoder(r.Body)
    var query Query
    err := dec.Decode(&query)
}
```

### Write Json

```go
type Result struct { 
    ID          int      `json:"id"`
    Name        string   `json:"name"`
    Description string   `json:"description"`
}

func (w http.ResponseWriter, r *http.Request) {
    var results []Result = model.GetResults() 
    enc := json.NewEncoder(w)
    err := enc.Encode(results)
}
```

## Built-in Response

* NotFound
* ServeFile
* ServeContent
* Redirect
