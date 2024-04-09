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
        "email": str(book["auther"]),
        "author": str(book["author"]),
        "catagory": str(book["catagory"])
    }



def list_book_serial(students) -> list:
    return [individual_book_serial(stu) for stu in students]


def individual_author_serial(author):
    return {
        "id": str(author["_id"]),
        "author name": str(author["name"])
    }


def list_author_serial(authors) -> list:
    return [individual_author_serial(author) for author in authors]


def individual_catagory_serial(catagory):
    return {
        "id": str(catagory["_id"]),
        "author name": str(catagory["name"])
    }


def list_catagory_serial(catagories) -> list:
    return [individual_catagory_serial(catagory) for catagory in catagories]
