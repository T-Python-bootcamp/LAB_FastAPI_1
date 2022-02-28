from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/students") 
def get_Student_Info():
    return {
        "Student1": {"Name":"Sara", "student_id":"123456", "GPA": "4.15/5"},
        "Student2": {"Name":"Amal", "student_id":"324567", "GPA": "4.75/5"}}
    
#-------------------------------------

@app.get("/students/{student_id}")
def read_item(student_id: int, level: Optional[str] = None):
    if level: 
        if student_id == 123456:
            return {"Name":"Sara", "student_id":"123456", "GPA": "4.15/5", "level": level}
        if      student_id == 324567:
            return  {"Name":"Amal", "student_id":"324567", "GPA": "4.75/5", "level": level} 
        else: 
            return {"student not found"}
    else:
        if student_id == 123456:
            return {"Name":"Sara", "student_id":"123456", "GPA": "4.15/5"}
        if      student_id == 324567:
            return  {"Name":"Amal", "student_id":"324567", "GPA": "4.75/5"}
        else: 
            return {"student not found"}
    
#--------------------------------------
    
students = [{"Name":"Sara", "student_id":"123456", "GPA": "4.15/5"}, 
            {"Name":"Amal", "student_id":"324567", "GPA": "4.75/5"}]
@app.get("/students/")
def read_item(skip: int = 0, limit: int = 2):
    return students[skip : skip + limit]

#---------------------------------------

@app.get("/students/req/{student_id}")
def read_user_item(student_id: str, name: str):
    student = {"student_id": student_id, "name": name}
    return student

# --------------------------------------

@app.get("/students/{student_id}/grades/{grade}")
async def read_user_item(
    student_id: int, grade: str, ps: str | None = None, short: bool = False
):
    student = {"student_id": student_id, "grade": grade}
    if ps:
        student.update({"side_note": ps})
    if not short:
        student.update(
            {"grade_message": f"This student's grade is {grade} in this semester"}
        )
    return student