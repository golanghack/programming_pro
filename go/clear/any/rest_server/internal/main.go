package main

import (
	"fmt"
	"html"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){
		fmt.Fprintf(w, "Wow, %q", html.EscapeString(r.URL.Path))
	}) 
	log.Println("Listen -> localhost:8000")
	log.Fatal(http.ListenAndServe(":8000", nil))
}