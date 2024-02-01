from datetime import datetime

from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(VARCHAR, unique=True, primary_key=True)
    rating = Column(Integer, default=0)
    registered = Column(DateTime, default=datetime.now())
