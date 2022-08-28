from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from mealsapp import db
from typing import List

from mealsapp.auth.jwt import get_current_user
from mealsapp.user import schema as userschema

from . import services

router = APIRouter(
    tags=['Init']
)


@router.on_event("startup")
async def startup_event(database=next(db.get_db())):
    await services.init_db_data(database)
