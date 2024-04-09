from pydantic import Field, BaseModel
from .students_model import StudentModel
from bson import ObjectId


class AuthorModel(BaseModel):
    id: str | None = None
    name: str


class CatagoryModel(BaseModel):
    id: str | None = None
    name: str = Field(max_length=20)


class BookModel(BaseModel):
    id: str | None = None
    name: str = Field(max_length=20)
    catagoryId: str | None = None
    authorId: str | None = None


class IssuedModel(BaseModel):
    id: str | None = None
    bookId: str | None = None
    studentId: str | None = None
    issued_date: str = Field(...)
    return_date: str = Field(...)