from datetime import date

from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, unique=True, primary_key=True)
    rating = Column(Integer, default=50)
    registered = Column(Date, default=date.today())
