# Database

## Connecting Database
1. Driver
2. sql.Open

在 main.go 中建立 db 不要在 model中建
1. 方便测试
2. 避免依赖，方便数据库的改数据底层

main.go
```go
func main() {
	templates := populateTemplates()
	db := connectToDatabase()  // return db 是为了方便关闭
	defer db.Close()
	controller.Startup(templates)
	http.ListenAndServe(":8000", &middleware.TimeoutMiddleware{new(middleware.GzipMiddleware)})
}

func connectToDatabase() *sql.DB {
	db, err := sql.Open("postgres", "postgres://lss:lss@localhost/lss?sslmode=disable")
	if err != nil {
		log.Fatalln(fmt.Errorf("Unable to connect to database: %v", err))
	}
	model.SetDatabase(db)
	return db
}
```

model/db.go
```go
package model

import "database/sql"

var db *sql.DB

func SetDatabase(database *sql.DB) {
	db = database
}
```

## Query

* Query
* QueryRow
* QueryContext
* QueryRowContext

```go
type Rows struct{}

func (*Rows) Close() error

func (*Rows) ColumnTypes() ([]*ColumnType, error)

func (*Rows) Columns() ([]string, error)

func (*Rows) Err() error

func (*Rows) Next() bool

func (*Rows) NextResultSet() bool

func (*Rows) Scan(dest ...interface{}) error

type Row struct{}

func (*Row) Scan(dest ...interface{}) error
```

## Update a Database

* Exec
* ExecContext

## Other Activity

* Ping
* PingContext
* Prepare
* PrepareContext
* Begin
* BeginTx