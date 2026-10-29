from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = f"sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_threads": False})

def create_table_and_database():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

class Base(DeclarativeBase):
    pass