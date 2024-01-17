#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False,)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False,)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete, delete-orphan',
                            backref='place')
    amenities = relationship('Amenity', secondary=place_amenity,
                                viewonly=False, back_populates="place_amenities")
    @property
    def reviews(self):
        """returns the list of Review instances with
        place_id equals to the current place.id
        """
        from models import storage
        from models.review import Review

        _all = storage.all(Review)
        result = []
        for instance in _all.values():
            if instance.place_id == self.id:
                result.append(instance)
        return result

    @property
    def amenities(self):
        """returns a list of Amenity instances based on the amenity_ids"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """a setter method for amenity_ids"""
        from models.amenity import Amenity
        if type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
