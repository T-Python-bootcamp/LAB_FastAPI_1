from fastapi import FastAPI
from typing import Optional
app = FastAPI()

student=[{"naem":"jamela" ,"id":1 ,"GPA":"99"},{"naem":"sara" ,"id":2 ,"GPA":"9"},
          {"naem":"maram" ,"id":44 ,"GPA":"33"},{"naem":"noura" ,"id":8 ,"GPA":"089"}]


@app.get("/get_Student_Info")
def students():
    return student
print("hay")


@app.get("/students")
async def students():
   return student





@app.get("/getStuden/{id}")
async def get_stedent(id:int):
   return {"id": id}



@app.get("/student/{id}")
def read_item(id: str, q: Optional[str] = None):
        if q:
         return {"id": id, "q": q}

         return {"id": id}
        else:
            return "nooo"

