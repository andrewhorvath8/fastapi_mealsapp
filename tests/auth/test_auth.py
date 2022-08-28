import pytest
from httpx import AsyncClient

from conf_test_db import app


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/login", data={"username": "test_login_user@test.com", "password": "123"})

    assert response.status_code == 200