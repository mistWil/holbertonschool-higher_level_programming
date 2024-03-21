#!/usr/bin/python3


"""Write a python file that contains the class definition of
a State and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """The State class inherits from Base, which means it
    gains all the attributes and methods from SQLAlchemy's Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
