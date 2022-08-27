from fastapi import HTTPException, status
from typing import List, Optional

from . import models
from . import validator


# Create a new user, check for unique email
async def new_user_register(request, database) -> models.User:
    user = await validator.get_user_by_email(request.email, database)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system."
        )
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


# List all users
async def list_all_users(database) -> List[models.User]:
    users = database.query(models.User).all()
    return users


# Get user by user id
async def get_user_by_id(user_id, database) -> Optional[models.User]:
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_info


# Update user by user id, user needs to exist
async def update_user_by_id(user_id, request, database) -> models.User:
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # If email in request is already present, only allow the change to go through, if it is same email for the user_id
    # This way you can change name without changing email
    user = await validator.get_user_by_email(request.email, database)
    if user:
        if user_info.email != request.email:
            raise HTTPException(
                status_code=400,
                detail="The user with this email already exists in the system."
            )

    user_info.name = request.name
    user_info.email = request.email

    database.commit()
    database.refresh(user_info)

    return user_info


# Delete a user by user id
async def delete_user_by_id(user_id, database):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
