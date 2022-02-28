from fastapi import FastAPI
from typing import Optional

app = FastAPI()


students = [
    {'student name:' : 'Haifa',
    'student ID:' : 7,
    'student GPA :' : '4.7 of 5.00'},
    {'student name:' : 'Haifaaa',
    'student ID:' : 5,
    'student GPA :' : '4.7 of 5.00'}
]


@app.get("/students")
async def get_Student_Info():
    return students


@app.get("/student/{student_id}")
def student_data(student_id : int):
    for student in students:
        if student['student ID:'] == student_id:
            return student


@app.get("/student-gpa/{student_id}")
def student_data(student_id : int , student_name: Optional[str] = None):
    if student_name:
        for student in students:
            if student['student ID:'] == student_id and student['student name:'] == student_name:
                return student
    else:
        for student in students:
            if student['student ID:'] == student_id:
                return student


@app.get("/student/{student_id}/gpa/{student_name}")
def show_student_data(student_id:int , student_name:str , show_all: bool = True):
    if show_all:
        for student in students:
            if student['student ID:'] == student_id and student['student name:'] == student_name:
                return student
    else:
        for student in students:
            if student['student ID:'] == student_id and student['student name:'] == student_name:
                return student['student ID:']