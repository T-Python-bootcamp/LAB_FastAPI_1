from fastapi import FastAPI 

app = FastAPI()





@app.get("/")
async def get_Student_Info():
    return {"Student Name" : "Mohammed",
            "Student ID":"123456", 
            "GPA" : 3.4,
            " " : "---------"} ,{
            "Student Name" : "Ahmed",
            "Student ID":"234567" , 
            "GPA" : 3.6 ,
            " " : "---------"
            }

@app.get("/students")
async def get_Student_Info():
    return {"Student Name" : "Mohammed",
            "student_id":123456, 
            "GPA" : 3.4} ,{
            "Student Name" : "Ahmed",
            "student_id":234567 , 
            "GPA" : 3.6
            }



@app.get("/students/{student_id}")
async def get_a_student(student_id: int):
    students = {
    1: {
        "Student Id":1 , 
        "Student Name" : "Ahmed",
        "GPA" : 3.6
    },
    2: {
        "Student Id": 2,
        "Student Name": "Peter",
        "GPA" : 3.6
    } ,  
    3: {
        "Student Id":3,
        "Student Name": "Ahmed",
        "GPA" : 3.6
    }
}
    return students[student_id]




# students = {
#     1: {
#         "Student Id":1 , 
#         "Student Name" : "Ahmed",
#         "GPA" : 3.6
#     },
#     2: {
#         "Student Id": 2,
#         "Student Name": "Peter",
#         "GPA" : 3.6
#     } ,  
#     3: {
#         "Student Id":3,
#         "Student Name": "Ahmed",
#         "GPA" : 3.6
#     } , 
#     4: {
#         "Student Id":4,
#         "Student Name": "Ahmed",
#         "GPA" : 3.6
#     } ,   
#     5: {
#         "Student Id":5,
#         "Student Name": "Ahmed",
#         "GPA" : 3.6
#     } , 
#     6: {
#         "Student Id":6,
#         "Student Name": "Ahmed",
#         "GPA" : 3.6
#     } , 
#     7: {
#         "Student Id":7,
#         "Student Name": "Ahmed",
#         "GPA" : 3.6
#     }
# }



