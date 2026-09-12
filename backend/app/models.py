from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column
from sqlalchemy import Text, Column, Date, Integer, Float, TIMESTAMP, DateTime, Enum, ForeignKey
import datetime

class Base(DeclarativeBase):
    pass

# Model of users SQL Table
class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    contact: Mapped[str]
    join_date: Mapped[datetime.date]

