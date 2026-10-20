from fastapi import FastAPI
import user
from database import engine
from routes import user_controller


user.base.metadata.create_all(bind = engine)


app = FastAPI(title= "Test Project")
app.include_router(user_controller.router)

app.include_router(user_controller.router_new)

