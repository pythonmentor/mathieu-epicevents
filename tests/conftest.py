import pytest



@pytest.fixture
def user_credentials_fixture():
    data = {"email": "sarah@gmail.com", "password":"essai"}
    return data