#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy.orm import relationship

Base = declarative_base()

place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String[60], ForeignKey('cities.id'), nullable=False)
    user_id = Column(String[60], ForeignKey('users.id'), nullable=False)
    name = Column(String[128], nullable=False)
    description = Column(String[1024], nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    #reviews = relationship("Review", cascade="delete, all", backref="place")
    #amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
