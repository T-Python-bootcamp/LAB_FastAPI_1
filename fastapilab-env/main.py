from typing import Optional
from fastapi import FastAPI

app = FastAPI()

students = [
    {
        "id": 1,
        "name": "Ali",
        "GPA": 90,
        "Books": [
            {
                "bookId": 123,
                "title": "Programming"
            },
            {
                "bookId": 345,
                "title": "Data Structure"
            }
        ]
    },
    {
        "id": 2,
        "name": "Turki",
        "GPA": 100,
        "Books": [
            {
                "bookId": 900,
                "title": "OP"
            },
            {
                "bookId": 768,
                "title": "System Analsys"
            }
        ]
    }
]


# Endpoint Get All Students Info
@app.get('/get_Students_Info')
def get_students():
    return students


# Just Change url path to /students
@app.get('/students')
def get_students():
    return students


# Creat an Endpoint to get Single student
@app.get("/get_a_student/{student_id}")
def get_student(student_id: int):
    for item in students:
        if item['id'] == student_id:
            return item
        else:
            return "Invalid student ID"


# Endpoint to test Required Parameters
@app.get('/requiredPara/{name}')
def root(name: str, GPA: int):
    return {"Student name is: ": name, "The GPA is: ": GPA}


# Endpoint to test Optional Parameters
@app.get('/optionalPara/{name}')
def root(name: str, GPA: Optional[int] = None):
    if GPA:
        return {"Student name is: ": name, "The GPA is: ": GPA}
    return {"Student name is: ": name}


# Endpoint for multiple path and query parameters
@app.get("/student/{student_id}/books/{book_id}")
def root(student_id: int, book_id: int, name: Optional[str] = None, GPA: Optional[int] = None):
    student = {"name": name, "GPA": GPA}
    for item in students:
        if item["id"] == student_id:
            for book in item["Books"]:
                if book["bookId"] == book_id:
                    return book
                return "Invalid student ID"
