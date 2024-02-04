from database import Base
from sqlalchemy import Column, String, Integer


class Post(Base):
    __tablename__ = "YourTable"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String,nullable=True)
    name = Column(String,nullable=True)
    cnic = Column(String,nullable=True)
    address = Column(String,nullable=True)