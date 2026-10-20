from pydantic import BaseModel

class UserCreateRequest(BaseModel):
    name: str
    email: str
    age: int
    email1: str
    age1: int
    email2: str
    age2: int


class SrudentCreateRequest(BaseModel):
    name: str
    father_name: str
    age: int
    email: str
    department: str
    student_Id: str
    marks: int

# class UserResponse(BaseModel):
#     id: int
#     name: str
#     email: str
#     age: int


class UserBase(BaseModel):
    name: str
    email: str
    age: int

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True 
        
#         (used to tell your model that it should be able to read data from ordinary
# objects, not just dictionaries)