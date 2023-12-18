#!/usr/bin/python3
"""
Definition of the City class.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    City class:
    - Inherits from Base.
    - Links to MySQL table cities.
    - Has id, name, and state_id attributes.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
