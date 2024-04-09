from fastapi import APIRouter
from main import db
from schema.schemas import list_book_serial, individual_book_serial
from models.book_model import BookModel
from bson import ObjectId

router = APIRouter(
    prefix="/books",
)


books_collection = db["books"]

@router.get("/")
async def get_all_books():
    all_books = books_collection.find()
    
    for book in all_books:
        book.author = books_collection.find_one({"_id": book.authorId}).name
    
    for book in all_books:
        book.catgory = books_collection.find_one({"_id": book.catagoryId}).name

    return list_book_serial(all_books)


@router.get("/{book_id}")
async def get_book_by_id(book_id: str):
    return list_book_serial(books_collection.find({"_id": ObjectId(book_id)}))


@router.post("/")
async def insert_book_details(book: BookModel):

    # books_collection.find_one({"_id": ObjectId(book.authorId)}).name
    return list_book_serial(books_collection.insert_one(dict(book)))