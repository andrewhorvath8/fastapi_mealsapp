from fastapi import APIRouter
from mealsapp import db

from . import services

router = APIRouter(
    tags=['Init']
)


@router.on_event("startup")
async def startup_event(database=next(db.get_db())):
    await services.init_db_data(database)
