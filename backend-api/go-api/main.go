package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Student struct {
	StudentID int    `json:"student_id"`
	Firstname string `json:"firstname"`
	Lastname  string `json:"lastname"`
	Address   string `json:"address"`
	Email     string `json:"email"`
}

var students []Student

func main() {
	http.HandleFunc("/students", handleStudents)
	fmt.Println("Golang API server listening on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleStudents(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		getStudents(w, r)
	case http.MethodPost:
		createStudent(w, r)
	case http.MethodPut:
		updateStudent(w, r)
	case http.MethodDelete:
		deleteStudent(w, r)
	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
		fmt.Fprintf(w, "Method not allowed")
	}
}

func getStudents(w http.ResponseWriter, _ *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(students)
}

func createStudent(w http.ResponseWriter, r *http.Request) {
	var student Student
	err := json.NewDecoder(r.Body).Decode(&student)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	students = append(students, student)
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(student)
}

func updateStudent(w http.ResponseWriter, r *http.Request) {
	// Implement update logic here
}

func deleteStudent(w http.ResponseWriter, r *http.Request) {
	// Implement delete logic here
}
