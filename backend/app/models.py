from sqlalchemy.orm import declarative_base, Mapped,mapped_column
from sqlalchemy import Text, Column, Date, Integer, Float, TIMESTAMP, DateTime, Enum, ForeignKey

class Base(declarative_base):
    pass

# Model of users SQL Table
class User():
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    contact: Mapped[str]
    join_date: Mapped[Date]

