from typing import Optional
from fastapi import FastAPI

app = FastAPI()

students = [
    {
        "id": 1,
        "name": "Yasser",
        "GPA": 95
    },
    {
        "id": 2,
        "name": "Careem",
        "GPA": 99.9
    }
]

teachers = [{
        "id": 1,
        "name": "Ali",
        "topic":"physics"
    },
    {
        "id": 2,
        "name": "Hamad",
        "topic":"literature"
    }]


# Part 1: An endpoint for all students data (static path)
@app.get('/students')
def get_Student_Info():
    return students


# Part 2: An endpoint for a specific student data based on the ID (dynamic path)
@app.get("/student/{studentID}")
def get_a_student(studentID: int):
    for item in students:
        if item['id'] == studentID:
            return item
    return {studentID:"Invalid"}
            


# Part 3: An Endpoint for required 
# Applied at a path like this:
# http://127.0.0.1:8000/part3/yasser?GPA=88
@app.get('/part3/{name}')
def root(name: str, GPA: int):
    return {"Name:": name, "GPA:": GPA}


# Part 4: An Endpoint for optional
# The path is similar to the previous one
# So it applied at a path like this:
# http://127.0.0.1:8000/part4/yasser?GPA=88
# Or http://127.0.0.1:8000/part4/yasser
@app.get('/part4/{name}')
def root(name: str, GPA: Optional[int] = None):
    if GPA:
        return {"Name:": name, "GPA:": GPA}
    return {"Name:":name}


# Part 5: An Endpoint for both
# Triggered on a path like:
# http://127.0.0.1:8000/student/2/teacher/2?name=yasser&GPA=100 
# or http://127.0.0.1:8000/student/2/teacher/2?name=yasser
# or http://127.0.0.1:8000/student/2/teacher/2
@app.get("/student/{studentID}/teacher/{teacherID}")
def root(studentID: int, teacherID: int, name: Optional[str] = None, GPA: Optional[int] = None):
    student = {}
    teacher = {}
    for item in students:
        if item["id"] == studentID:
            student=item
    for item in teachers:
        if item["id"] == teacherID:
            teacher = item
    if student and teacher:
        return {"Name and GPA":{name,GPA},"S ID":student,"T ID":teacher}
    else:
        return {"invalid":{"Student ID":studentID,"Teacher ID":teacherID,"Name":name,"GPA":GPA}}
    