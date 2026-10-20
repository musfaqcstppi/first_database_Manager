from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 


# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/new_db_my"
DATABASE_URL = "postgresql+psycopg2://training_jls0_user:h3daqQFGBaycKf2aK9n9iL5SaFIPJiA6@dpg-dbbfgmeq1p3s73cefugg-a.oregon-postgres.render.com/training_jls0"

engine = create_engine(DATABASE_URL)
localSession = sessionmaker(autocommit = False, autoflush=False, bind=engine)
base = declarative_base()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

