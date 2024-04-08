package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Data struct {
	Message string `json:"message"`
}

func handler(w http.ResponseWriter, r *http.Request) {
	data := Data{Message: "Hello this my web api project"}
	json.NewEncoder(w).Encode(data)
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Golang API server listening on port 8080...")
	http.ListenAndServe(":8080", nil)
}
