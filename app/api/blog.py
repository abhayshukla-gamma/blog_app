from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.models.Blogs import Blog
from app.core.jwt import decode_access_token
from fastapi.security import OAuth2PasswordBearer
from app.schemas.blog import BlogCreate, BlogUpdate
from app.core.security import get_current_user

router = APIRouter(prefix="/blog", tags=["Blog Api"])

@router.post("/add")
def create_blog(blog : BlogCreate, current_user : User = Depends(get_current_user), db : Session = Depends(get_db)):

# current_user : User = Depends(get_current_user)    to fetch the current user 
    new_blog = Blog(
        title = blog.title,
        content = blog.content,
        user_id = current_user.id

    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return {
        "message" : "blog added"
    }


@router.get("/getblogs")
def get_all_blogs(db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    blogs = db.query(Blog).all()

    return blogs


@router.get("/blogs/{blog_id}")
def get_single_blog(blog_id : int, db : Session = Depends(get_db),current_user: User = Depends(get_current_user)):

    blog = db.query(Blog).filter(Blog.blog_id== blog_id).first()

    if blog.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    
    return blog


@router.put("/update/{blog_id}")
def update_blog(blog_id : int, updated_data : BlogUpdate,current_user: User = Depends(get_current_user), db : Session = Depends(get_db)):

    blog = db.query(Blog).filter(Blog.blog_id == blog_id).first()

    if blog.user_id != current_user.id:
      raise HTTPException(status_code=403, detail="Not authorized")

    blog.title = updated_data.title
    blog.content = updated_data.content

    db.commit()
    db.refresh(blog)

    return blog 


@router.delete("/delete/{blog_id}")
def delete_blog(blog_id, current_user: User = Depends(get_current_user), db : Session = Depends(get_db)):

    blog = db.query(Blog).filter(Blog.blog_id == blog_id).first()

    if blog.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")


    if not blog:
        raise HTTPException(status_code=404, detail="id not found")
    
    db.delete(blog)

    db.commit()

    return {
        "message" : "blog deleted"
    }
    