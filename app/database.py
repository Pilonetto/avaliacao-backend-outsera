from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool
from app.models import Movie
import csv
import os

engine = create_engine(
    "sqlite://",
    echo=False,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def load_data_from_csv(filepath: str):
    print(filepath)
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        movies = []

        for row in reader:
            movie = Movie(
                year=int(row["year"]),
                title=row["title"],
                studios=row["studios"],
                producers=row["producers"],
                winner=row["winner"].strip().lower() == "yes"
            )
            movies.append(movie)

        with Session(engine) as session:
            session.add_all(movies)
            session.commit()