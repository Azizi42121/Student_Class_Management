from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import select
from app.core.database import SessionDep
from app.schemas.class_model import Class
from app.schemas.class_model import BuatKelas, EditKelas, ResponseKelas, ResponseKelasDenganSiswa

router = APIRouter(prefix="/classes", tags=["Classes"])

# Membuat kelas baru
@router.post("/", response_model=ResponseKelas, status_code=201)
def create_class(data: BuatKelas, db: SessionDep):
    db_class = Class.model_validate(data)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

# Mengambil semua kelas
@router.get("/", response_model=List[ResponseKelas], status_code=200)
def get_all_class(db: SessionDep):
    classes = db.exec(select(Class)).all()
    return classes

# Mengambil daftar siswa di kelas tertentu
@router.get("/{class_id}/student", response_model=ResponseKelasDenganSiswa)
def get_class_detail(class_id: int, db: SessionDep):
    db_class = db.get(Class, class_id)
    if not db_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kelas tidak ditemukan"
        )

    return db_class