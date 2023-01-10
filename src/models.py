import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User (Base):
    __tablename__ = 'user'
    id =Column(Integer, primary_key=True)
    username = Column(String(200))
    first_name = Column(String (200))
    last_name = Column (String(200))
    email = Column (String(200))


class Post (Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    description = Column(String(200))

class Follow (Base): 
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    follower_userid = Column(Integer, ForeignKey("user.id"))
    following_user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Media (Base): 
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
