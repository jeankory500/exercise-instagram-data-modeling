import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), unique=True)
    email = Column(String(75), nullable=False)
    name = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_Id = Column(Integer, ForeignKey('user.id'))
    #media_Id = Column(Integer, ForeignKey('media.id'))
    #comments_Id = Column(Integer, ForeignKey('comments.id'))
    def to_dict(self):
        return {}
    
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(500))
    post_id = Column(Integer, ForeignKey('post.id'))
    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable= False)
    author_Id = Column(Integer, ForeignKey('user.id'))
    post_Id = Column(Integer, ForeignKey('post.id'))
    #media_id = Column(Integer, ForeignKey('media.id'))
    def to_dict(self):
        return {}


                     

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
