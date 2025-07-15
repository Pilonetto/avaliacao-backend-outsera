from sqlmodel import SQLModel, Field
from typing import Optional


class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    year: int
    title: str
    studios: str
    producers: str
    winner: bool = Field(default=False)