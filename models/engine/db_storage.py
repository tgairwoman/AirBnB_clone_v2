from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base, BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class DBStorage:
    """a database storage for hbnb"""
    __engine = None
    __session = None

    def __init__(self):
        """Initiations of the DBStorage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(os.getenv(
                'HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'), os.getenv(
                    'HBNB_MYSQL_HOST'), os.getenv(
                        'HBNB_MYSQL_DB')), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session
        (self.__session) all objects depending of
        the class name (argument cls)
        """
        result = {}
        if cls:
            instances = self.__session.query(cls)
            for instance in instances:
                key = "{}.{}".format(instance.__class__.__name__, instance.id)
                result[key] = instance
        else:
            objects = [State, City, User]
            for obj in objects:
                instances = self.__session.query(obj)
                for instance in instances:
                    key = "{}.{}".format(
                        instance.__class__.__name__, instance.id)
                    result[key] = instance
        return result

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=True)
        Session = scoped_session(session_factory)
        self.__session = Session()
