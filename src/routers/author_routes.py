from fastapi import APIRouter, HTTPException
from main import db
from schema.schemas import list_author_serial
from bson import ObjectId
from models.book_model import AuthorModel

author_collection = db['authors']

router = APIRouter(
    prefix="/authors",
    tags=['author'],
    responses={
        "data": {
            "msg": "error occuered"
        }
    }
)

@router.get("/", status_code=200)
async def get_all_authors():
    authors_list = list_author_serial(author_collection.find())

    return {
        "message": "successfully fetched all authors details",
        "Status": 200,
        "data": authors_list
    }


@router.get("/{author_id}", status_code=200)
async def get_author(author_id: str):
    author = author_collection.find({"_id": ObjectId(author_id)})

    if not author:
        raise HTTPException(404, {"error": "Sorry no author found"})
    
    return {
        "message": "successfully fetched all authors details",
        "Status": 200,
        "data": list_author_serial(author)
    }


@router.post("/", status_code=201)
async def insert_author(auth: AuthorModel):
    author = author_collection.find_one({"name": auth.name})

    if author:
        raise HTTPException(401, {"error": "Author details already present"})
    
    author_obj = author_collection.insert_one(dict(auth))
    auth.id = str(author_obj.inserted_id)

    return {
        "message": "Author detail inserted successfully",
        "status": 201,
        "auther id": auth.id
    }


@router.delete("/", status_code=200)
async def delete_author(auth: AuthorModel):
    author = author_collection.find_one({"name": auth.name})

    if not author:
        raise HTTPException(401, {"error": "Author details Does not found"})
    
    author_collection.delete_one({"name": auth.name})
    auth.id = None

    return {
        "message": "Author detail deleted successfully",
        "status": 201,
    }