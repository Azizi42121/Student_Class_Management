from sqlmodel import SQLModel
from typing import Optional
from app.schemas.class_model import ResponseKelas

# request body saat menambah siswa baru
class BuatSiswa(SQLModel):
    student_number: str
    full_name: str
    class_id: int

# response body standar siswa
class ResponsesSiswa():
    id: int

class SiswaWithClassResponse(ResponsesSiswa):
    classroom: Optional[ResponseKelas] = None