from operator import index
from turtle import title
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.db import Base


class HomeWork(Base):
    __tablename__ = "home_works"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='home_works')