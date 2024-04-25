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
    if not student_id:
        raise HTTPException(
            status_code=404, 
            detail={'error': 'student id cannot be 2'}
        )
    
    return {
        "message": "student details fetched successfully",
        "status": 200,
        "data": list_serial(student_collection.find({"_id": ObjectId(student_id)}))
    }


@router.post("/", status_code=201, tags=["student"], summary="Insert student details")
async def insert_student_details(stud: StudentModel):
    student = student_collection.find_one(filter={"email": str(stud.email)})

    if student:
        raise HTTPException(401, detail={"error": "student already exists"})
    
    res = student_collection.insert_one(dict(stud))
    stud.id = str(res.inserted_id)
    
    return {
        "message": "Student data inserted successfully",
        "status": 201,
        "student id": str(res.inserted_id)
    }

@router.delete("/{stud_id}", status_code=200)
async def delete_student_details(stud_id: str):

    fetch_student = student_collection.find_one(filter={"_id": ObjectId(stud_id)})

    if not fetch_student:
        raise HTTPException(404, {"error": "no student exists"})
    
    student_collection.delete_one({"_id": ObjectId(stud_id)})

    return {
        "success": "Student record deleted successfully",
        "status": 200
    }