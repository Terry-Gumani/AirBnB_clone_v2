#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
# from models import storage_type
from models.city import city
from sqlalchemy import Column, String
# from models import storage_type


class State(BaseModel, Base):
    """ State class/ table model """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False) if models.storage_t == 'db' else ""

        @property
        def cities(self):
            from models import storage
            related_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
