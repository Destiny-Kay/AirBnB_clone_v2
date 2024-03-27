#!/usr/bin/python3
"""Defines a DB storage engine"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """An engine to manage database storage mechanisms"""
    __engine = None
    __session = None

    def __init__(self):
        sql_user = getenv("HBNB_MYSQL_USER")
        sql_pass = getenv("HBNB_MYSQL_PWD")
        sql_host = getenv("HBNB_MYSQL_HOST")
        sql_db = getenv("HBNB_MYSQL_DB")
        conn_params = f"mysql+mysqldb://{sql_user}:{sql_pass}@{sql_host}/{sql_db}"
        self.__engine = create_engine(conn_params, pool_pre_ping=True)

        test_env = getenv("HBNB_ENV")
        if test_env == "test":
            Base.metadata.drop_all(self.__engine)
   
    def all(self, cls=None):
        """Queries the database and reeturns all models as dict"""
        objects = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for e in query:
                key = "{}.{}".format(type(e).__name__, e.id)
                objects[key] = e
        else:
            models = [State, City, User, Place, Review, Amenity]
            for model in models:
                query = self.__session.query(model)
                for e in query:
                    key = "{}.{}".format(type(e).__name__, e.id)
                    objects[key] = e
        return objects
    
    def new(self, obj):
        """Adds a new record to the table"""
        self.__session.add(obj)
    
    def save(self):
        """Saves a record to DB"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """deletes records in DB"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """DB configuration"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
    
    def close(self):
        """closes a DB session"""
        self.__session.remove()
