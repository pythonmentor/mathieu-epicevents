import pytest
from tests import conftest
from controllers.login_manager import AuthenticationAndPermissions
from views.get_datas import GetDatas


class MockResponse:
    @staticmethod
    def get_credentials():
        email = "s@g.c"
        password = "e"
        return email, password


class TestLogin:

    def test_check_password(self, monkeypatch):
        def mock_get(*args, **kwargs):
            return MockResponse()

        monkeypatch.setattr("views.get_datas.GetDatas", mock_get)

        sut = AuthenticationAndPermissions()
        sut.check_password()

        assert sut.menu.choice_main_menu()


