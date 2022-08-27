from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from typing import List

from mealsapp import db
from mealsapp.auth.jwt import get_current_user
from . import schema
from . import services

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)


# Create a new user
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    return await services.new_user_register(request, database)


# List all users
@router.get('/', response_model=List[schema.DisplayUser])
async def get_all_users(database: Session = Depends(db.get_db),
                        current_user: schema.User = Depends(get_current_user)):
    return await services.list_all_users(database)


# Get a user by user id
@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                         current_user: schema.User = Depends(get_current_user)):
    return await services.get_user_by_id(user_id, database)


# Update an existing user identified by user id
@router.put('/{user_id}', response_model=schema.DisplayUser)
async def update_user_by_id(user_id: int, request: schema.ModifyUser, database: Session = Depends(db.get_db),
                            current_user: schema.User = Depends(get_current_user)):
    return await services.update_user_by_id(user_id, request, database)


# Delete a user identified by user id
@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                            current_user: schema.User = Depends(get_current_user)):
    return await services.delete_user_by_id(user_id, database)
