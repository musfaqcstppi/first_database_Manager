from sqlalchemy.orm import Session
from user import User, Student_info

class UserRepository:
    def create_user(self,db: Session, model: User):
        db.add(model)
        db.commit()
        db.refresh(model)
        return model
    
    def student_create_user(self,db: Session, model: Student_info):
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

    def get_by_email(self, db: Session, email: str):
        return db.query(Student_info).filter(Student_info.email == email).first()
        
    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    
    def get_all(self, db: Session):
        db_users=  db.query(Student_info).all()
        return db_users
    
    def delete_by_email(self, db:Session, email:str):
        del_user = db.query(Student_info).filter(Student_info.email==email).first()
        if del_user:
            db.delete(del_user)
            db.commit()


















    # def delete(self, db: Session, user):
    #         db.delete(user)
    #         db.commit()
    
    
    # def create(self, db: Session, user: schemas.UserCreate):
    #     db_user = models.User(name=user.name, email=user.email, age=user.age)
    #     db.add(db_user)
    #     db.commit()
    #     db.refresh(db_user)
    #     return db_user
    
    # def update(self, db: Session, user_id: int, updated_data: schemas.UserCreate):
    #     user_query = db.query(models.User).filter(models.User.id == user_id)
    #     user_query.update(updated_data.model_dump(), synchronize_session=False)
    #     db.commit()
    #     return user_query.first()
    
    