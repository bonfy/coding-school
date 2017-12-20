package main

import (
	"html/template"
	"log"
	"net/http"
)

func main() {
	templates := populateTemplates()
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		requestFile := r.URL.Path[1:]
		t := templates.Lookup(requestFile + ".html")
		if t != nil {
			err := t.Execute(w, nil)
			if err != nil {
				log.Println(err)
			}
		} else {
			w.WriteHeader(http.StatusNotFound)
		}
	})

	http.Handle("/img/", http.FileServer(http.Dir("../public")))
	http.Handle("/css/", http.FileServer(http.Dir("../public")))
	http.ListenAndServe(":8888", nil)
}

func populateTemplates() *template.Template {
	result := template.New("templates")
	basePath := "../templates"

	// file, _ := exec.LookPath(os.Args[0])
	// path, _ := filepath.Abs(file)
	// pathList := strings.Split(path, "/")
	// length := len(pathList)
	// path = filepath.Join(pathList[:length-2]...)
	// path = filepath.Join(path, "templates")

	template.Must(result.ParseGlob(basePath + "/*.html"))
	return result
}
