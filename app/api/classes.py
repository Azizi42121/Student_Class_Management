from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import select
from app.core.database import SessionDep
from app.models.class_student import Kelas
from app.schemas.class_model import BuatKelas, EditKelas, ResponseKelas, ResponseKelasDenganSiswa

router = APIRouter(prefix="/classes", tags=["Classes"])

# Membuat kelas baru
@router.post("/", response_model=ResponseKelas, status_code=201)
def create_class(data: BuatKelas, db: SessionDep):
    db_class = Kelas.model_validate(data)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

# Mengambil semua kelas
@router.get("/", response_model=List[ResponseKelas], status_code=200)
def get_all_class(db: SessionDep):
    classes = db.exec(select(Kelas)).all()
    return classes

# Mengambil daftar siswa di kelas tertentu
@router.get("/{class_id}/student", response_model=ResponseKelasDenganSiswa)
def get_class_detail(class_id: int, db: SessionDep):
    db_class = db.get(Kelas, class_id)
    if not db_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kelas tidak ditemukan"
        )

    return db_class

# Edit data kelas parsial (hanya nama dan ruangannya)
@router.put("/{class_id}", response_model=ResponseKelas)
def update_class(class_id: int, data: EditKelas ,db: SessionDep):
    db_class = db.get(Kelas, class_id)
    if not db_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kelas tidak ditemukan"
        )

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_class, key, value)

    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

# menghapus kelas
@router.delete("/{class_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_class(class_id: int, db: SessionDep):
    db_class = db.get(Kelas, class_id)
    if not db_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kelas tidak ditemukan"
        )

    db.delete(db_class)
    db.commit()
    return None