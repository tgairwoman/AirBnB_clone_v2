#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """getter attribute that gets all cities whith the current State."""
        from models import storage
        _cities = storage.all(City)
        result = {}
        for key, value in _cities.items():
            if value.id == self.id:
                result[key] = value
        return result
