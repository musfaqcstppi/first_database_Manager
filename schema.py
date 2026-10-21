from pydantic import BaseModel

class UserCreateRequest(BaseModel):
    name: str
    email: str
    age: int
    address: str
    marks: int
    department: str
    roll: int


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