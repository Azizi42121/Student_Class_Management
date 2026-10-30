from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import select
from app.core.database import SessionDep
from app.schemas.student import Class
from app.schemas.student import BuatSiswa, ResponseSiswa, SiswaWithClassResponse

router = APIRouter(prefix="/students", tags=["Students"])

# lanjut membuat routenya
# post("/") menambah siswa baru
# get("/") mengambil semua siswa (dengan pagination & filter)
# put("/{student_id}") mengubah data siswa atau pindah kelas
# delete("/{student_id}") menghapus siswa