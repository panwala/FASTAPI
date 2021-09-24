from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

students = {
    1: {
        "name": "prem",
        "age": 22
    }
}


class Student(BaseModel):
    name: str
    age: int


class updateStudents(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


@app.get("/")
def index():
    return {"name": "Prem Manojkumar Panwala"}


@app.get("/get_students")
def studentDetails():
    return students


@app.get("/get_single_student/{studentId}")
def singleStudentByPath(studentId: int):
    return students[studentId]


@app.get("/get_single_student_by_query")
def singleStudentByQuery(studentId: int):
    return students[studentId]


@app.post("/create-student/{student_Id}")
def createStudent(student_Id: int, student: Student):

    students[student_Id] = student

    return students[student_Id]


@app.put("/update-student/{student_Id}")
def updateStudent(student_Id: int, student: updateStudents):

    if student.name != None:
        students[student_Id].name = student.name

    if student.age != None:
        students[student_Id].age = student.age
    return students[student_Id]
