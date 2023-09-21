#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models import storage_type


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    isdb = storage_type == 'db'
    name = Column(string(128), nullable=False) if isdb else ""
    state_id = Column(string(60),
                      ForeignKey('states.id'),
                      nullable=False) if isdb else ""
