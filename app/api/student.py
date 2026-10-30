from fastapi import APIRouter, HTTPException, status, Query
from typing import List
from sqlmodel import select, func
from app.core.database import SessionDep
from app.schemas.student import Class
from app.schemas.student import BuatSiswa, ResponseSiswa, SiswaWithClassResponse, PaginatedStudentResponse

router = APIRouter(prefix="/students", tags=["Students"])

# lanjut membuat routenya

# post("/") menambah siswa baru
@router.post("/",response_model=ResponseSiswa)
def create_student(data: BuatSiswa, db: SessionDep):
    db_student = Class.model_validate(data)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# get("/") mengambil semua siswa (dengan pagination & filter)
@router.get("/", response_model=PaginatedStudentResponse)
def get_all_students(db: SessionDep, page: int = Query(1, ge=1, description="Nomor halaman"), size: int = Query(10, ge=1, le=100, description="Jumlah item per halaman"), search: str | None = Query(None, description="Cari nama atau nomor siswa"), class_id: int | None = Query(None, description="Filter berdasarkan ID kelas")):
    # Base Query
    statement = select(Class)
    count_statement = select(func.count()).select_from(Class)

    # Filter berdasarkan pencarion nama atau nomor siswa
    if search:
        filter_condition  = (Class.full_name.ilike(f"%{search}%")) | (Class.student_number.ilike(f"%{search}%"))
        statement = statement.where(filter_condition)
        count_statement = count_statement.where(filter_condition)

    # Filter berdasarkan kelas
    if class_id:
        statement = statement.where(Class.class_id == class_id)
        count_statement = count_statement.wher(Class.class_id == class_id)

    # Hitung total data sebelum pagination
    total = db.exec(count_statement).one()

    # eksekusi pagination (offset & limit)
    offset = (page - 1) * size
    statement = statement.offset(offset).limit(size)
    students = db.exec(statement).all()

    return {
        "total": total,
        "page": page,
        "size": size,
        "results": students
    }

# put("/{student_id}") mengubah data siswa atau pindah kelas
# delete("/{student_id}") menghapus siswa