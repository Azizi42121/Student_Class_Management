from sqlmodel import SQLModel

# request body untuk menambah kelas baru
class BuatKelas(SQLModel):
    name: str
    room: str

# response body untuk mengembalikan data kelas
class ResponseKelas(BuatKelas):
    id: int