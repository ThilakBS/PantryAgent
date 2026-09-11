import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv #Import .env values

load_dotenv() #load .env values

d_base = os.environ["DATABASE_URL"]

#establish connection to Supabase session
engine = create_engine(d_base)
session = sessionmaker(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
