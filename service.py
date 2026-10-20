from repository import UserRepository
from sqlalchemy.orm import Session
from schema import UserCreateRequest, SrudentCreateRequest
from user import User, Student_info

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, db:Session, user_payload: UserCreateRequest):
        user = User(name= user_payload.name,
                    email = user_payload.email,
                    age = user_payload.age,
                    email1 = user_payload.email,
                    age1 = user_payload.age,
                    email2 = user_payload.email,
                    age2 = user_payload.age)
        self.user_repository.create_user(db, user)


    def student_create_user(self, db:Session, user_payload: SrudentCreateRequest):
        user_Student = Student_info(name= user_payload.name,
                    father_name = user_payload.father_name,
                    age = user_payload.age,
                    email = user_payload.email,
                    department = user_payload.department,
                    student_Id = user_payload.student_Id,
                    marks = user_payload.marks)
        self.user_repository.student_create_user(db, user_Student)


    def get_all_users(self, db:Session):
        return self.user_repository.get_all(db)
    

    def get_user_by_email(self, db:Session,email:str):
        return self.user_repository.get_by_email(db,email)

    def delete_by_email(self,db:Session, email:str):
        self.user_repository.delete_by_email(db,email)
        return "Deleted Successfully"


