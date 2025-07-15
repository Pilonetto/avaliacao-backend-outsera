from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_db_and_tables, load_data_from_csv
from app.routers import router



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    load_data_from_csv("Movielist.csv")
    yield
    # não executar nada ao finalizar

app = FastAPI(lifespan=lifespan, title="Golden Raspberry Awards API (outsera)")


#por mais que seja apenas uma rota, usei a classe APIRouter que serve para organizar melhor a api mesmo que nesse cenário não fosse necessário
app.include_router(router)