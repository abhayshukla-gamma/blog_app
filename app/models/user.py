from sqlalchemy import Column ,String, Integer,Float,Boolean
from app.db.base import Base
from sqlalchemy.orm import relationship



class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String,unique=True,index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # blogs = relationship("Blog", back_populates="author")

