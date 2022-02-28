
from fastapi import FastAPI,Query
from typing import Optional
from enum import Enum


app = FastAPI()
students = [{"Student_Name":"Sara", "Student_ID":123456,"GPA":88.45}, {"Student_Name":"lama", "Student_ID":654321,"GPA":99.99},
{"Student Name":"lmal", "Student ID":987654,"GPA":95.9}]


# Create an API “get_Student_Info” returns student information:

# - Student Name
# - Student ID
# - GPA

# Change the path of “get_Student_Info” to “/students”

@app.get("/students")
def get_Student_Info():
    return students


# Create an API “get_a_student” 

# - it returns student information based on student_id 
# - Use dynamic path parameters to change the path to student_id
# - Change path parameter with type integer

@app.get("/students/{student_id}")
def get_a_student(student_id :int):
    index=0
    while True:
        if students[index]["Student_ID"] == student_id:
            return students[index]
        index=index+1


#Create an API that applies required, optional and query parameters 
#       
@app.get("/items")
def read_item(name: str, id: Optional[int] = None, ):
    if id:
        return {"name": name, "id": id}

    return {"name": name}

#Create an API that applies multiple path and query parameters as the following  
#     
@app.get("/items/{name}/id/{id}")
def read_item(name: str, id: int, last_name: str):
    return {"name": name, "id": id, "last_name": last_name}

# Use a regular expression with query parameter.

@app.get("/regular/")
async def read_items(
    path: str | None = Query(None, min_length=3, max_length=50, regex="^python$")
):
    results = {"students": [{"name": "nouf"}, {"name": "wala"}]}
    if path:
        results.update({"path": path})
    return results

#Path convertor

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

#Python enumerations

class studentsName(str, Enum):
    student1 = "nouf"
    student2 = "sara"
    student3 = "maram"
    
@app.get("/student/{student_name}")
async def get_model(student_name: studentsName):
    if student_name == studentsName.student1:
        return {"student_name": student_name, "message": "he/she first student"}

    if student_name.value == "sara":
        return {"student_name": student_name, "message": "he/she second student"}

    return {"student_name": student_name, "message": "he/she last student"}