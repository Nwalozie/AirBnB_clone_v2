#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
import models
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:

        @property
        def cities(self):
            """ Returns the list of City instances with
            state_id == current State.id """
            all_cities = models.storage.all(City)
            state_cities = []
            for city_ins in all_cities.values():
                if city_ins.state_id == self.id:
                    state_cities.append(city_ins)

            return state_cities
