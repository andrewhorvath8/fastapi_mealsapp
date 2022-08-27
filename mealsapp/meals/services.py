from fastapi import HTTPException, status
from typing import List, Optional
from . import models


async def create_new_meal(request, database) -> models.Meals:
    new_meal = models.Meals(
        name=request.name,
        price=request.price,
        ingredients=request.ingredients,
        spicy=request.spicy,
        vegan=request.vegan,
        gluten_free=request.gluten_free,
        description=request.description,
        kcal=request.kcal,
        image=request.image
    )
    database.add(new_meal)
    database.commit()
    database.refresh(new_meal)
    return new_meal


async def get_all_meals(database) -> List[models.Meals]:
    meals = database.query(models.Meals).all()
    return meals


async def get_meal_by_id(meal_id, database) -> Optional[models.Meals]:
    meal_info = database.query(models.Meals).get(meal_id)
    if not meal_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meal not found!")
    return meal_info


async def update_meal_by_id(meal_id, request, database) -> Optional[models.Meals]:
    meal_info = database.query(models.Meals).get(meal_id)
    if not meal_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meal not found!")

    meal_info.name = request.name
    meal_info.price = request.price
    meal_info.ingredients = request.ingredients
    meal_info.spicy = request.spicy
    meal_info.vegan = request.vegan
    meal_info.gluten_free = request.gluten_free
    meal_info.description = request.description
    meal_info.kcal = request.kcal
    meal_info.image = request.image

    database.commit()
    database.refresh(meal_info)

    return meal_info


async def delete_meal_by_id(meal_id, database):
    database.query(models.Meals).filter(models.Meals.id == meal_id).delete()
    database.commit()
