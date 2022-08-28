import pytest

from mealsapp.user.models import User
from conf_test_db import override_get_db


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """Fixture to execute asserts before and after a test is run"""
    # Setup
    database = next(override_get_db())
    new_login_user = User(
        name="test_login_user",
        email="test_login_user@test.com",
        password="123"
    )

    database.add(new_login_user)
    database.commit()
    database.refresh(new_login_user)

    yield

    # Teardown
    database.query(User).filter(User.email == 'test_login_user@test.com').delete()
    database.commit()
