from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column
from sqlalchemy import Text, Column, Date, Integer, Float, TIMESTAMP, DateTime, Enum, ForeignKey
import datetime
import enum
from typing import Optional

class Base(DeclarativeBase):
    pass

# Model of users SQL Table
class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    contact: Mapped[str]
    join_date: Mapped[datetime.date]

# Model of pantry SQL Table
class units(enum.Enum):
    mL = 'mL'
    L = 'L'
    g ='g'
    kg ='kg'
    oz ='oz'
    lb ='lb'
    count ='count'

class cate(enum.Enum):
    meat = 'meat'
    veg='veg'
    fruit='fruit'
    frozen='frozen'
    drinks='drinks'
    snacks='snacks'
    dry='dry'
    mis='mis'


class Pantry(Base):
    __tablename__ = 'pantry'

    obj_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    food_name: Mapped[str]
    quantity: Mapped[float]
    unit: Mapped[units]
    date_added: Mapped[datetime.date]
    expiration: Mapped[Optional[datetime.date]]
    category: Mapped[cate]

