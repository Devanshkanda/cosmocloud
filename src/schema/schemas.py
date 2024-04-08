def individual_serial(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": str(student["name"]),
        "email": str(student["email"]),
        "phone": str(student["phone_number"]),
        "batch": str(student["batch_year"]),
        "course": str(student["course"])
    }



def list_serial(students) -> list:
    return [individual_serial(stu) for stu in students]