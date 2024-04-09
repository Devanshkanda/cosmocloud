from fastapi import APIRouter, HTTPException
from main import db
from schema.schemas import list_catagory_serial
from bson import ObjectId
from models.book_model import CatagoryModel

catagory_collection = db['catagory']

router = APIRouter(
    prefix="/catagory",
    tags=['author'],
    responses={
        "data": {
            "msg": "error occuered"
        }
    }
)

@router.get("/", status_code=200)
async def get_all_catagory():
    catagory_list = list_catagory_serial(catagory_collection.find())

    return {
        "message": "successfully fetched all catagories details",
        "Status": 200,
        "data": catagory_list
    }


@router.get("/{catagory_id}", status_code=200)
async def get_catagory(catagory_id: str):
    catagory = catagory_collection.find({"_id": ObjectId(catagory_id)})

    if not catagory:
        raise HTTPException(404, {"error": "Sorry no catagory found"})
    
    return {
        "message": "successfully fetched catagory details",
        "Status": 200,
        "data": list_catagory_serial(catagory)
    }


@router.post("/", status_code=201)
async def insert_catagory(catagory: CatagoryModel):
    catagory = catagory_collection.find_one({"name": catagory.name})

    if catagory:
        raise HTTPException(401, {"error": "Author details already present"})
    
    catagory_obj = catagory_collection.insert_one(dict(catagory))
    catagory.id = str(catagory_obj.inserted_id)

    return {
        "message": "Author detail inserted successfully",
        "status": 201,
        "auther id": catagory.id
    }


@router.delete("/{catagory_id}", status_code=200)
async def delete_author(catagory_id):
    catagory = catagory_collection.find_one({"_id": ObjectId(catagory_id)})

    if not catagory:
        raise HTTPException(401, {"error": "Catagory details Does not found"})
    
    catagory_collection.delete_one({"_id": catagory_id})
    # auth.id = None

    return {
        "message": "Author detail deleted successfully",
        "status": 201,
    }