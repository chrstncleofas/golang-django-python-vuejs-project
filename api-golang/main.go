package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

type Students struct {
	StudentID string `json:"studentID"`
	FirstName string `json:"firstName"`
	LastName  string `json:"lastName"`
	Address   string `json:"address"`
	Email     string `json:"email"`
}

var students = []Students{
	{StudentID: "1", FirstName: "John", LastName: "Doe", Address: "123 Main St", Email: "john@example.com"},
	{StudentID: "2", FirstName: "Jane", LastName: "Smith", Address: "456 Elm St", Email: "jane@example.com"},
}

func getAllStudents(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(students)
}

func getStudent(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	for _, item := range students {
		if item.StudentID == params["id"] {
			json.NewEncoder(w).Encode(item)
			return
		}
	}
	json.NewEncoder(w).Encode(&Students{})
}

func createStudent(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var student Students
	_ = json.NewDecoder(r.Body).Decode(&student)
	students = append(students, student)
	json.NewEncoder(w).Encode(student)
}

func updateStudent(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	for index, item := range students {
		if item.StudentID == params["id"] {
			students[index] = Students{
				StudentID: params["id"],
				FirstName: "Updated Firstname",
				LastName:  "Updated Lastname",
				Address:   "Updated Address",
				Email:     "updated@example.com",
			}
			json.NewEncoder(w).Encode(students[index])
			return
		}
	}
	json.NewEncoder(w).Encode(students)
}

func deleteStudent(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	for index, item := range students {
		if item.StudentID == params["id"] {
			students = append(students[:index], students[index+1:]...)
			break
		}
	}
	json.NewEncoder(w).Encode(students)
}

func main() {
	router := mux.NewRouter()
	router.HandleFunc("/students", getAllStudents).Methods("GET")
	router.HandleFunc("/students/{id}", getStudent).Methods("GET")
	router.HandleFunc("/students", createStudent).Methods("POST")
	router.HandleFunc("/students/{id}", updateStudent).Methods("PUT")
	router.HandleFunc("/students/{id}", deleteStudent).Methods("DELETE")
	log.Fatal(http.ListenAndServe(":8000", router))
}
