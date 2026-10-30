from fastapi import APIRouter
from typing import List
from sqlmodel import select
from app.core.database import SessionDep
from app.schemas.class_model import BuatKelas, ResponseKelas, Class

router = APIRouter(prefix="/classes", tags=["Classes"])

