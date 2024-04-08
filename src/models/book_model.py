from pydantic import Field, BaseModel
from .students_model import StudentModel


class BookModel(BaseModel):
    name: str = Field(max_length=20)
    catagory = Field(...)
    author = Field(...)


class AuthorModel(BaseModel):
    name: str = Field(max_length=20)


class CatagoryModel(BaseModel):
    name: str = Field(max_length=20)


class IssuedModel(BaseModel):
    book: BookModel = Field(...)
    student_id: StudentModel = Field(...)
    issued_date = Field(...)
    return_date = Field(...)