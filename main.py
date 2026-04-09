from fastapi import FastAPI
from data_model import NewStudent
from data_model import UpdateStudent
app = FastAPI(
    title="CRUD operations",
    description="API for CRUD operations"
)
students = {
    1: { "name":"anil",
        "age":19
        }
}
@app.get("/")
def index():
    return "Welcome to the API: CRUD operations"
@app.get("/students")
def get_students():
    return students

@app.get("/student/{stu_id}")
def get_student(stu_id: int):
    if stu_id not in students:
        return f"No student found with student id = {stu_id}"
    return students[stu_id]

@app.post("/add-student")
def add_student(stu: NewStudent):
    if not students:
        new_id = 1
    else:
        new_id = max(students.keys()) + 1
    students[new_id] = stu.model_dump()
    return students[new_id]

@app.put("/update-student/{stu-id}")
def update_student(stu_id: int,stu:UpdateStudent):
    if stu_id not in students:
        return f"No student found with student id = {stu_id}"
    if stu.name is not None:
        students[stu_id]["Name"] = stu.name
    if stu.age is not None:
        students[stu_id]["age"] = stu.age    
    return students[stu_id]

@app.delete("/delete-student/{stu_id}")
def delete_student(stu_id : int):
    if stu_id not in students:
        return f"No student found with student id = {stu_id}"
    del students[stu_id]
    return students
