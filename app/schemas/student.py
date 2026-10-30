from sqlmodel import SQLModel
from typing import Optional, List
from app.schemas.class_model import ResponseKelas

# request body saat menambah siswa baru
class BuatSiswa(SQLModel):
    student_number: str
    full_name: str
    class_id: int

# response body standar siswa
class ResponseSiswa(BuatSiswa):
    id: int

class SiswaWithClassResponse(ResponseSiswa):
    classroom: Optional[ResponseKelas] = None

class PaginatedStudentResponse(SQLModel):
    total: int
    page: int
    size: int
    result: List[SiswaWithClassResponse]