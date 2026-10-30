from sqlmodel import SQLModel
from typing import Optional, List
from app.schemas.student import ResponseSiswa

# request body untuk menambah kelas baru
class BuatKelas(SQLModel):
    name: str
    room: str

# request untuk edit kelas
class EditKelas(SQLModel):
    name: Optional[str] = None
    room: Optional[str] = None

# response body untuk mengembalikan data kelas
class ResponseKelas(BuatKelas):
    id: int

# response detail (dipakai di Get /classes/{class_id})
class ResponseKelasDenganSiswa(ResponseKelas):
    students = List[ResponseSiswa] = []