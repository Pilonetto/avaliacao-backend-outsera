from fastapi import APIRouter
from app.services import get_award_intervals

router = APIRouter()


@router.get("/producers/interval-awards")
def interval_awards():
    return get_award_intervals()
