#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(VARCHAR(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)