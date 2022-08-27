import pytest
from httpx import AsyncClient

from mealsapp.user.models import User
from conf_test_db import app, override_get_db


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        database = next(override_get_db())
        new_user = User(
            name="test_login_user",
            email="test_login_user@test.com",
            password="123"
        )

        database.add(new_user)
        database.commit()

        print("\n\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n")
        mod_user = database.query(User).get(new_user.id)
        print(f"{mod_user.name}\n\n")

        response = await ac.post("/login", data={"username": "test_login_user@test.com", "password": "123"})

    assert response.status_code == 200