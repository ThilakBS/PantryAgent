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
class u(enum.Enum):
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

# Model of convos SQL Table
class Convos(Base):
    __tablename__ = 'convos'

    convo_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    ses_time: Mapped[datetime.datetime]
    title: Mapped[Optional[str]]

# Model of messages SQL Table
class roles(enum.Enum):
    user = 'user'
    assistant = 'assistant'


class Messages(Base):
    __tablename__ = 'messages'

    mes_id: Mapped[int] = mapped_column(primary_key=True)
    convo_id: Mapped[int] = mapped_column(ForeignKey("convos.convo_id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    mes_role: Mapped[roles]
    content: Mapped[str]
    convo_time: Mapped[datetime.datetime]

# Model of tool sql table
class tools(Base):
    __tablename__ = 'tools'

    call_id: Mapped[int] = mapped_column(primary_key=True)
    mes_id: Mapped[int] = mapped_column(ForeignKey("messages.mes_id"))
    tool_name: Mapped[str]

# Model of expiration sql table
class expiration(Base):
    __table_name__ = 'exp_alert'

    alert: Mapped[int] = mapped_column(primary_key=True)
    obj_id: Mapped[int] = mapped_column(ForeignKey("pantry.obj_id"))
    alerted: Mapped[datetime.datetime]

# Model of recipie history SQL table
class recipe_history(Base):
    __table_name__ = 'recipe_history'

    recipe_id: Mapped[int] = mapped_column(primary_key=True)
    convo_id: Mapped[int] = mapped_column(ForeignKey("convos.convo_id"))
    recipe_name: Mapped[str]