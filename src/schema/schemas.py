def individual_student_serial(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": str(student["name"]),
        "email": str(student["email"]),
        "phone": str(student["phone_number"]),
        "batch": str(student["batch_year"]),
        "course": str(student["course"])
    }



def list_serial(students) -> list:
    return [individual_student_serial(stu) for stu in students]


def individual_book_serial(book) -> dict:
    return {
        "id": str(book["_id"]),
        "name": str(book["name"]),
        "email": str(book["auther"])
    }



def list_book_serial(students) -> list:
    return [individual_book_serial(stu) for stu in students]