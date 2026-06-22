```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()

class Student(BaseModel):
    id:int
    name:str =Field(min_length=3,max_length=10)
    age:int =Field(gt=0)
    email:Optional[str]=None

students = []

@app.post("/students")
def create_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student Created",
        "student": student
    }

@app.get("/students")
def get_students():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: dict):

    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = updated_student
            return {
                "message": "Student Updated",
                "student": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )

@app.patch("/students/{student_id}")
def patch_student(student_id: int, data: dict):

    for student in students:
        if student["id"] == student_id:
            student.update(data)

            return {
                "message": "Student Updated Successfully",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)

            return {
                "message": "Student Deleted Successfully",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )


```
