from typing import Optional
from fastapi import FastAPI




my_list=[{"name":"othman","studentid":123,"gpa":4.39,"itmes":1},{"name":"mohamd","studentid":4344,"gpa":2.34,"itmes":2}
]

app = FastAPI()



@app.get("/")
def stati():
    return {"massege":"static is done!"}




@app.get("/students/{student_id}")
def inf_student(student_id:int):
    for x in my_list:
        if x["studentid"] == student_id:
            return x
        else:
            return "student not found"



@app.get("/students-gpa/{student_id}")
def int_stude(student_id: int, name: Optional[str] = None):
    if name:
        for x in my_list:
            if x["studentid"]== student_id and x["name"]==name:
                return x 
    else:
            for y in my_list:
                y["name"]==name and y["studentid"]== student_id 
                return y





@app.get("/students/{student_id}/itms/{itms_id}")
def items(student_id:int,itms_id:int):
    if student_id:
        for x in my_list:
            if x["studentid"]==student_id and x["itmes"]==itms_id:
                return x




















