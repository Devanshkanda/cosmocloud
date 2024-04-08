from pydantic import BaseModel, Field, EmailStr, ConfigDict


class StudentModel(BaseModel):
    id: str = Field(alias="_id", default=None)
    name: str
    course: str 
    batch_year: str
    email: EmailStr
    phone_number: int

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra= {
            "example": {
                "name": "devansh kanda",
                "course": "BCA",
                "batch_year": "2023",
                "email": "dk@gmail.com",
                "phone_number": 1234567890
            }
        }
    )