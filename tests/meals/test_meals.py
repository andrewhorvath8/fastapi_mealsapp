import pytest
from httpx import AsyncClient
from sqlalchemy.orm.exc import ObjectDeletedError

from mealsapp.auth.jwt import create_access_token
from mealsapp.meals.models import Meals
from conf_test_db import app, override_get_db


# Test creating a new meal
@pytest.mark.asyncio
async def test_new_meal():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "TestUser@testuser.com"})
        database = next(override_get_db())
        payload = {
            "name": "test_new_meal",
            "price": 101,
            "ingredients": "test es test",
            "spicy": "True",
            "vegan": "True",
            "gluten_free": "True",
            "description": "test meal",
            "kcal": 1000,
            "image": "0"
        }

        response = await ac.post("/meals/", json=payload, headers={'Authorization': f'Bearer {user_access_token}'})

        db_meal = database.query(Meals).filter(Meals.name == "test_new_meal").first()

    assert response.status_code == 201
    assert response.json()['name'] == "test_new_meal"
    assert response.json()['price'] == 101.0
    assert response.json()['ingredients'] == "test es test"
    assert response.json()['spicy'] == True
    assert response.json()['vegan'] == True
    assert response.json()['gluten_free'] == True
    assert response.json()['description'] == "test meal"
    assert response.json()['kcal'] == 1000.0
    assert response.json()['image'] == "0"
    assert db_meal.name == "test_new_meal"
    assert db_meal.price == 101.0
    assert db_meal.ingredients == "test es test"
    assert db_meal.spicy == True
    assert db_meal.vegan == True
    assert db_meal.gluten_free == True
    assert db_meal.description == "test meal"
    assert db_meal.kcal == 1000.0
    assert db_meal.image == b'0'


# Test listing meals function
@pytest.mark.asyncio
async def test_list_all_meal():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "TestUser@testuser.com"})
        response = await ac.get("/meals/", headers={'Authorization': f'Bearer {user_access_token}'})
    assert response.status_code == 200
    assert 'name' in response.json()[0]
    assert 'price' in response.json()[0]
    assert 'ingredients' in response.json()[0]
    assert 'spicy' in response.json()[0]
    assert 'vegan' in response.json()[0]
    assert 'gluten_free' in response.json()[0]
    assert 'description' in response.json()[0]
    assert 'kcal' in response.json()[0]
    assert 'image' in response.json()[0]


# Test getting a meal by id
@pytest.mark.asyncio
async def test_get_meal_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "TestUser@testuser.com"})
        database = next(override_get_db())
        new_meal = Meals(
            name="test_meal",
            price=101.0,
            ingredients="test es test",
            spicy=True,
            vegan=True,
            gluten_free=True,
            description="test meal",
            kcal=1000.0,
            image=b'0'
        )

        database.add(new_meal)
        database.commit()

        db_meal = database.query(Meals).get(new_meal.id)

        response = await ac.get(f"/meals/{new_meal.id}", headers={'Authorization': f'Bearer {user_access_token}'})

    assert response.status_code == 200
    assert response.json()['name'] == "test_meal"
    assert response.json()['price'] == 101.0
    assert response.json()['ingredients'] == "test es test"
    assert response.json()['spicy'] == True
    assert response.json()['vegan'] == True
    assert response.json()['gluten_free'] == True
    assert response.json()['description'] == "test meal"
    assert response.json()['kcal'] == 1000.0
    assert response.json()['image'] == "0"
    assert db_meal.name == "test_meal"
    assert db_meal.price == 101.0
    assert db_meal.ingredients == "test es test"
    assert db_meal.spicy == True
    assert db_meal.vegan == True
    assert db_meal.gluten_free == True
    assert db_meal.description == "test meal"
    assert db_meal.kcal == 1000.0
    assert db_meal.image == b'0'


# Test updating a meal by id
@pytest.mark.asyncio
async def test_update_meal_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "TestUser@testuser.com"})
        database = next(override_get_db())
        new_meal = Meals(
            name="test_meal",
            price=101.0,
            ingredients="test es test",
            spicy=True,
            vegan=True,
            gluten_free=True,
            description="test meal",
            kcal=1000.0,
            image=b'0'
        )

        payload = {
            "name": "test_meal_mod",
            "price": 102,
            "ingredients": "test_meal_mod",
            "spicy": "False",
            "vegan": "False",
            "gluten_free": "False",
            "description": "test_meal_mod",
            "kcal": 1001,
            "image": "0 1"
        }

        database.add(new_meal)
        database.commit()

        response = await ac.put(f"/meals/{new_meal.id}", json=payload,
                                headers={'Authorization': f'Bearer {user_access_token}'})
        # database.expire_all()
        database.refresh(new_meal)
        mod_meal = database.query(Meals).get(new_meal.id)

    assert response.status_code == 200
    assert response.json()['name'] == "test_meal_mod"
    assert response.json()['price'] == 102.0
    assert response.json()['ingredients'] == "test_meal_mod"
    assert response.json()['spicy'] == False
    assert response.json()['vegan'] == False
    assert response.json()['gluten_free'] == False
    assert response.json()['description'] == "test_meal_mod"
    assert response.json()['kcal'] == 1001.0
    assert response.json()['image'] == "0 1"
    assert mod_meal.name == "test_meal_mod"
    assert mod_meal.price == 102.0
    assert mod_meal.ingredients == "test_meal_mod"
    assert mod_meal.spicy == False
    assert mod_meal.vegan == False
    assert mod_meal.gluten_free == False
    assert mod_meal.description == "test_meal_mod"
    assert mod_meal.kcal == 1001.0
    assert mod_meal.image == b'0 1'


# Test deleting a meal by id
@pytest.mark.asyncio
async def test_delete_meal_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "TestUser@testuser.com"})
        database = next(override_get_db())
        new_meal = Meals(
            name="deleted_meal_by_id",
            price=801.0,
            ingredients="deleted_meal",
            spicy=True,
            vegan=True,
            gluten_free=True,
            description="deleted_meal",
            kcal=9000.0,
            image=b'0'
        )

        database.add(new_meal)
        database.commit()

        response = await ac.delete(f"/meals/{new_meal.id}", headers={'Authorization': f'Bearer {user_access_token}'})

        database.expire_all()

    assert response.status_code == 204
