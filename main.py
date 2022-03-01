from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/students")
async def get_Student_Info():
    return {"student1": {"name": "mohmmad", "id": 3705968, "gpa": 4.03}}, {
        "student2": {"name": "eyad", "id": 394534, "gpa": 3.88}}


@app.get("/students/{id}")
async def get_a_student(id: int):
    students = {1: {"name": "mohmmad",
                        "id": 1,
                        "gpa": 4.03}, 
                            
                2: {"name": "eyad",
                        "id": 2,
                        "gpa": 3.88}}
    return students[id]


