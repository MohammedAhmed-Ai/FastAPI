

# app = FastAPI()

# @app.get("/")
# async def read_home():
#     return {"message": "Welcome "}

# @app.get("/about")
# async def read_about():
#     return {"message": "This is the About Page"}

# @app.get("/contact")
# async def read_contact():
#     return {"message": "This is the Contact Page"}

# @app.get("/services")
# async def read_services():
#     return {"message": "This is the Services Page"}

# products_db = {
#     "products": [
#         {"id": 1, "name": "Product A", "price": 100},
#         {"id": 2, "name": "Product B", "price": 150},
#         {"id": 3, "name": "Product C", "price": 200},
#     ]
# }

# @app.get("/products")
# async def read_products():
#     return {"message": products_db["products"]}

# @app.get("/help")
# async def read_help():
#     return {"message": "This is the Help Page"}

# @app.post("/faq")
# async def read_faq():
#     return {"message": "This is the FAQ Page"}

# class Products(BaseModel):
#     id: int
#     name: str
#     price: int

# @app.post("/products")
# async def add_product(product: Products):
#     products_db["products"].append(
#         {
#             "id": product.id,
#             "name": product.name,
#             "price": product.price
#         }
#     )
#     return {
#         "message": "Product created successfully",
#         "product": product
#     }

# @app.get("/predict")
# async def predict_result():
#     return {"message": "accuracy 90%"}



# @app.get("/culculate_pmi")
# async def culculate_pmi(w:int,h:int):
#     pmi = w / (h * h)
#     return {"pmi": pmi}





from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class students(BaseModel):
    id:int
    name:str
    age:int
    grade:str
students_db=[
    students(id=1,name="Alice",age=14,grade="9th"),
    students(id=2,name="Bob",age=15,grade="10th"),
]

@app.get("/students")
async def get_students():
    return students_db

@app.post("/students")
async def add_studants(student:students):
    students_db.append(student)
    return {
        "message":"Student added successfully",
        "student":student
    }

@app.put("/students/{student_id}")
async def update_student(student_id:int,updated_student:students):
    for index,student in enumerate(students_db):
        if student.id==student_id:
            students_db[index]=updated_student
            return {
                "message":"Student updated successfully",
                "student":updated_student
            }
    return {"message":"Student not found"}


@app.delete("/students/{student_id}") 
async def delete_student(student_id:int):
    for index,student in enumerate(students_db):
        if student.id==student_id:
            deleted_student=students_db.pop(index)
            return {
                "message":"Student deleted successfully",
                "student":deleted_student
            }
    return {"message":"Student not found"}
