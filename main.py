from fastapi import FastAPI
from typing import Optional

app = FastAPI()

students = {
    1111: {"name": "Mohammad","id": "1111", "gpa": 3.77, "grades": {"cs233": 74, "cs401": 90}}, 
    2222: {"name": "Khaled","id": "2222", "gpa": 4.2, "grades": {"cs233": 81, "cs401": 88}},
    3333: {"name": "Salem","id": "3333", "gpa": 3.5, "grades": {"cs233": 70, "cs401": 83}}
    }


@app.get("/students")
async def get_Student_Info():
    return students


@app.get("/student/{student_id}")
async def get_a_student(student_id: int):
    if student_id in students:
        return students[student_id]
    else:
        return "Invalid user ID"


@app.get("/students/{student_id}/grade/{course}")
async def get_a_student_grade(student_id: int, course: Optional[str] = None, q: Optional[str] = None):
    if student_id in students:
        if q == "json" and course in students[student_id]["grades"]:
            return {"grade": students[student_id]["grades"][course]} 
        elif course in students[student_id]["grades"]:
            return students[student_id]["grades"][course]
        else:
            return "This students doesn't has the selected course"
    else:
        return "Invalid student ID"

    