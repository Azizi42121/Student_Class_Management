from fastapi import APIRouter
from typing import List
from sqlmodel import select
from app.core.database import SessionDep
from app.schemas.class_model import BuatKelas, ResponseKelas, Class

router = APIRouter(prefix="/classes", tags=["Classes"])

# Membuat kelas baru
@router.post("/", response_model=ResponseKelas, status_code=201)
def create_class(data: BuatKelas, db: SessionDep):
    db_class = Class.model_validate(data)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

