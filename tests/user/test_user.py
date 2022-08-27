import pytest
from httpx import AsyncClient

from mealsapp.auth.jwt import create_access_token
from conf_test_db import app, override_get_db
from mealsapp.user.models import User


@pytest.mark.asyncio
async def test_get_all_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "TestUser@testuser.com"})
        response = await ac.get("/user/", headers={'Authorization': f'Bearer {user_access_token}'})
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_user_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "TestUser@testuser.com"})

        database = next(override_get_db())
        new_user = User(
            name="test_update_user",
            email="test_update_user@test.com",
            password="123"
        )

        payload = {
            "name": "test_update_user_mod",
            "email": "test_update_user_mod@test.com"
        }

        database.add(new_user)
        database.commit()

        response = await ac.put(f"/user/{new_user.id}", json=payload,
                                headers={'Authorization': f'Bearer {user_access_token}'})

        database.expire_all()

        mod_user = database.query(User).get(new_user.id)

    assert response.status_code == 200
    assert response.json()['name'] == "test_update_user_mod"
    assert response.json()['email'] == "test_update_user_mod@test.com"
    assert mod_user.name == "test_update_user_mod"
    assert mod_user.email == "test_update_user_mod@test.com"


@pytest.mark.asyncio
async def test_delete_user_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "TestUser@testuser.com"})

        database = next(override_get_db())
        new_user = User(
            name="test_delete_user",
            email="test_delete_user@test.com",
            password="123"
        )

        database.add(new_user)
        database.commit()
        database.refresh(new_user)

        response = await ac.delete(f"/user/{new_user.id}", headers={'Authorization': f'Bearer {user_access_token}'})

    assert response.status_code == 204
