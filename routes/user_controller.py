from fastapi import APIRouter, Depends, status
from schema import UserCreateRequest, SrudentCreateRequest
from database import get_db
from service import UserService
from sqlalchemy.orm import Session



router = APIRouter(
    prefix="/user"
)

@router.post("/create")
def create_user(user_payload : UserCreateRequest, db:Session = Depends(get_db)):
    user_service = UserService()
    user_service.create_user(db, user_payload)

@router.get("/list")
def get_all_users(db: Session = Depends(get_db)):
    student_user_service = UserService()
    return student_user_service.get_all_users(db)

@router.get("/{email}")
def get_user_by_email(email:str, db:Session = Depends(get_db)):
    service_new= UserService()
    return service_new.get_user_by_email(db,email)

@router.delete("{/delete}")
def delete_user_by_email(email:str, db:Session = Depends(get_db)):
    delete_service= UserService()
    return delete_service.delete_by_email(db,email)





router_new = APIRouter(
    prefix=""
)

@router_new.post("/student_create")
def student_create_user(student_payload: SrudentCreateRequest, db: Session = Depends(get_db)):
    student_user_service = UserService()
    student_user_service.student_create_user(db, student_payload)


