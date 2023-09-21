#!/usr/bin/python3
"""
Contains the class DBStorage
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    """A class to manage DB storage via MYSQL and SQLAlchemy"""
