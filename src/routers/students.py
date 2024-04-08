from fastapi import APIRouter, HTTPException
from models.students_model import StudentModel
from schema.schemas import individual_student_serial, list_serial
from bson import ObjectId
from main import db


student_collection = db['student']

router = APIRouter(
    prefix="/students",
    tags=['students'],
    responses={
        "data": {
            "msg": "error occuered"
        }
    }
)


@router.get("/", status_code=200, summary="fetch all student details")
async def get_all_student_detail():
    """
    Fetch all users details
    """

    student_details = list_serial(student_collection.find())

    return {
        "message": "Student records fetched successfully",
        "status": 200,
        "data": student_details
    }


@router.get("/{student_id}", status_code=200)
async def get_student_detail(student_id: str):
    if student_id == 2:
        raise HTTPException(status_code=404, detail={'error': 'student id cannot be 2'})
    return {
        "mesg": "student details fetched successfully",
        "data": list_serial(student_collection.find({"_id": ObjectId(student_id)}))
    }


@router.post("/", status_code=201, tags=["student"], summary="Insert student details")
async def insert_student_details(stud: StudentModel):
    # if stud.id in StudentModel:
    #     raise HTTPException(
    #         status_code=401, 
    #         detail={"error": "Student detail already present"}
    #     )
    
    res = student_collection.insert_one(dict(stud))
    
    return {
        "success": list_serial(res)
    }