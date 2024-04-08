# Django Golang CRUD Application

## Introduction

This project is an example of a CRUD (Create, Read, Update, Delete) application using Django on the backend and Golang to create a RESTful API.

## Requirements

- Python 3.7+
- Poetry
- PostgreSQL
- Golang

## Setup

1. **Clone the Repository:** Clone the repository using git:

    ```bash
    git clone https://github.com/your_username/your_project.git
    cd your_project
    ```

2. **Set Up the Virtual Environment:** Use Poetry to set up a virtual environment and install the dependencies:

    ```bash
    poetry install
    ```

3. **Migrate the Database:** Migrate the database migrations for your Django application:

    ```bash
    poetry run python manage.py migrate
    ```

4. **Run the Golang Server:** Navigate to the directory of your Golang server and execute it using the Go compiler:

    ```bash
    cd golang_server
    go run main.go
    ```

5. **Run the Django Server:** Back in the directory of your Django application, execute the Django server using this command:

    ```bash
    poetry run python manage.py runserver 127.0.0.1:8080
    ```

6. **Access the Application:** Open your web browser and go to `http://127.0.0.1:8080/` to access your Django application.

## API Endpoints

- `/api/students/`: GET - Retrieve all students
- `/api/student/<student_id>/`: GET - Retrieve details of a student
- `/api/student/`: POST - Create a new student
- `/api/student/<student_id>/`: PUT - Update details of a student
- `/api/student/<student_id>/`: DELETE - Delete a student
