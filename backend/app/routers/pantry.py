from fastapi import FastAPI, APIRouter, Request, Depends
from pydantic import BaseModel
from database import get_db
from models import Pantry
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/pantry")
def get_pantry_items(db: Session = Depends(get_db)):
    return db.query(Pantry).all()
