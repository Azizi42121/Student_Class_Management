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

class UpdateSiswa(SQLModel):
    student_number = Optional[int] = None
    full_name = Optional[str] = None
    class_id = Optional[int] = None

class SiswaWithClassResponse(ResponseSiswa):
    classroom: Optional[ResponseKelas] = None

class PaginatedStudentResponse(SQLModel):
    total: int
    page: int
    size: int
    result: List[SiswaWithClassResponse]