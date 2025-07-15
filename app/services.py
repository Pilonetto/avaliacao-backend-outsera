from sqlmodel import Session, select
from app.models import Movie
from app.database import engine
from collections import defaultdict
from typing import Dict, List


def get_award_intervals() -> Dict[str, List[Dict]]:
    # primeiro... pegar só quem já venceu 
    with Session(engine) as session:
        winners = session.exec(select(Movie).where(Movie.winner == True)).all()

    # criar um dict onde usarei como chave o nome
    producer_years = defaultdict(list)

    for movie in winners:
        # alguns nomes estao separados por virgulas e outros por "and" então faço um replace no and para virgula
        producers = movie.producers.replace(" and ", ",").split(",")
        for producer in [p.strip() for p in producers if p.strip()]:
            producer_years[producer].append(movie.year) # aqui ta adicionando o ano que venceu ao nome do produtor

    intervals = []

    for producer, years in producer_years.items():
        # se não ganhou ao menos dois, não precisa processar
        if len(years) < 2: 
            continue

        sorted_years = sorted(years)
        for i in range(1, len(sorted_years)):
            intervals.append({
                "producer": producer,
                "interval": sorted_years[i] - sorted_years[i - 1],
                "previousWin": sorted_years[i - 1],
                "followingWin": sorted_years[i]
            })

    if not intervals:
        return {"min": [], "max": []}

    min_interval = min(i["interval"] for i in intervals)
    max_interval = max(i["interval"] for i in intervals)

    return {
        "min": [i for i in intervals if i["interval"] == min_interval],
        "max": [i for i in intervals if i["interval"] == max_interval],
    }
