
# Code 1

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


# version 2

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field,EmailStr,field_validator,ConfigDict
from typing import Optional, Annotated,List
import re

app = FastAPI()

NameType=Annotated[
    str,
    Field(
        min_length=3,
        max_length=10
    )
]
class Course(BaseModel):
    name:str
    duration:int
class Address(BaseModel):
    city:str
    state:str
class Student(BaseModel):
    model_config=ConfigDict(frozen=True)
    id: int
    name: str=Field(alias="fullName")
    age: int = Field(gte=18, le=60)
    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=20,
        description="Password must contain uppercase, lowercase, digit, and special character"
    )

    courses: List[Course]
    address: Address
    skills: List[str]

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")

        if " " in value:
            raise ValueError("Password must not contain spaces")

        return value
    @field_validator("email")
    @classmethod
    def validate_company_email(cls,value):
        if not value.endswith("@bytexl.in"):
            raise ValueError("use company email")
        return value

class Trainer(BaseModel):
    id:int
    name:NameType

class StudentResponse(BaseModel):
    id: int
    name: str
    age:int



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

@app.get("/students/{id}",response_model=StudentResponse)
def get_students(id:int):
    return {
        "id":id,
        "name":"Ravi",
        "age":18
    }
```
