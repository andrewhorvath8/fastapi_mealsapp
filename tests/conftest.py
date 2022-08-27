import pytest

from mealsapp.user.models import User
from conf_test_db import override_get_db


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want
    database = next(override_get_db())
    # new_login_user = User(
    #     name="test_login_user",
    #     email="test_login_user@test.com",
    #     password="123"
    # )
    #
    # database.add(new_login_user)
    # database.commit()

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want
    database.query(User).filter(User.email == 'test_login_user@test.com').delete()
    database.commit()
