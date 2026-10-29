from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Kelas(SQLModel, table=True):
    __tablename__ = "kelas"

    id: Optional[int] = Field(default=None)
    name: str
    room: str

    students: List["Siswa"] = Relationship(back_populates="classroom")

class Siswa(SQLModel, table=True):
    __tablename__ = "siswa"

    id: Optional[int] = Field(default=None, primary_key=True)
    student_number: str = Field(unique=True, index=True)
    full_name: str

    class_id: Optional[int] = Field(default=None, foreign_key="kelas.id")

    classroom = Optional[Kelas] = Relationship(back_populates="students")
