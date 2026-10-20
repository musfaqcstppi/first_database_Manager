from sqlalchemy import Column, Integer, String
from database import base

class User(base):
    __tablename__="users"
    __table_args__ = {"schema":"new_db_my"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100))
    age = Column(String(100))
    email1 = Column(String(100))
    age1 = Column(String(100))
    email2 = Column(String(100))
    age2 = Column(String(100))


class Student_info(base):
    __tablename__="student_info"
    __table_args__ = {"schema":"new_db_my"}

    name = Column(String(100))
    father_name = Column(String(100))
    age = Column(Integer)
    email = Column(String(100))
    department = Column(String(100))
    student_Id= Column(Integer, primary_key=True, autoincrement=True)
    marks = Column(Integer)


