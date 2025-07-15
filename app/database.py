from sqlmodel import SQLModel, Session, create_engine
from app.models import Movie
import csv
import os

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables():
    # deleta o banco para não duplicar os dados durante os testes
    if os.path.exists("database.db"):
        os.remove("database.db")
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
            print(row["title"])
            movies.append(movie)

        with Session(engine) as session:
            session.add_all(movies)
            session.commit()
            print("commit")