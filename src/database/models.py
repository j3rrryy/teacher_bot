from datetime import date

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = sa.Column(sa.BIGINT, unique=True, primary_key=True)
    rating = sa.Column(sa.INTEGER, default=50)
    registered = sa.Column(sa.DATE, default=date.today())

    def __str__(self) -> str:
        return f"<User: {self.id}>"

    def columns_to_dict(self) -> dict:
        d = {key: getattr(self, key) for key in self.__mapper__.c.keys()}
        return d
