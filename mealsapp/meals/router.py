from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from mealsapp import db
from typing import List

from mealsapp.auth.jwt import get_current_user
from mealsapp.user import schema as userschema

from . import schema
from . import services

# from . import validator

router = APIRouter(
    tags=['Meals'],
    prefix='/meals'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_new_meal(request: schema.Meal, database: Session = Depends(db.get_db),
                          current_user: userschema.User = Depends(get_current_user)):
    new_meal = await services.create_new_meal(request, database)
    return new_meal


@router.get('/', response_model=List[schema.DisplayMeal])
async def get_all_meals(database: Session = Depends(db.get_db),
                        current_user: userschema.User = Depends(get_current_user)):
    return await services.get_all_meals(database)


@router.get('/{meal_id}', response_model=schema.DisplayMeal)
async def get_meal_by_id(meal_id: int, database: Session = Depends(db.get_db),
                         current_user: userschema.User = Depends(get_current_user)):
    return await services.get_meal_by_id(meal_id, database)


@router.put('/{meal_id}', response_model=schema.DisplayMeal)
async def update_meal_by_id(meal_id: int, request: schema.Meal, database: Session = Depends(db.get_db),
                            current_user: userschema.User = Depends(get_current_user)):
    return await services.update_meal_by_id(meal_id, request, database)


@router.delete('/{meal_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_meal_by_id(meal_id: int, database: Session = Depends(db.get_db),
                            current_user: userschema.User = Depends(get_current_user)):
    return await services.delete_meal_by_id(meal_id, database)
