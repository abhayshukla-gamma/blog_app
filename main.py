from fastapi import FastAPI
from app.db.session import engine
from app.models.user import User
from app.db.base import Base
from dotenv import load_dotenv
from app.api import auth
from app.models.Blogs import Blog
from app.api import blog

load_dotenv()
Base.metadata.create_all(bind=engine)


app = FastAPI()

Base.metadata.create_all(bind=engine)   
app.include_router(auth.router)
app.include_router(blog.router)

@app.get("/")
def index():
    return {"message " : "project is running "}