#!/usr/bin/python3
"""contains the class definition of a
State and an instance Base = declarative_base()
"""


#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """sub class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
