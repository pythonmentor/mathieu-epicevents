from unittest.mock import call

from controllers import login_manager

FAKE_PASSWORD = "12345"
FAKE_HASHED_PASSWORD = (
    "$argon2id$v=19$m=65536,t=3,p=4$AcB4D8GYc27tnRPinNM6hw$2PfVv4W"
    "H1CoD0/TWmyDw2z0iBTj++WAVt/G9IJRnvtg"
)


class TestLogin:
    def test_check_password(self, mocker):
        mocker.patch("controllers.login_manager.Menu")
        mocker.patch("controllers.login_manager.Messages")
        MockGetDatas = mocker.patch("controllers.login_manager.GetDatas")
        MockGetDatas.return_value.get_credentials.return_value = (
            "me@example.com",
            FAKE_PASSWORD,
        )

        mock_session = mocker.patch("controllers.login_manager.SESSION")
        mock_staff_user = (
            mock_session.query.return_value.filter.return_value.one_or_none.return_value
        )
        mock_staff_user.password = FAKE_HASHED_PASSWORD
        mock_staff_user.department.name = "test_departement"

        mock_create_token = mocker.patch(
            "controllers.login_manager.AuthenticationAndPermissions.create_token"
        )
        MockMenuManager = mocker.patch("controllers.login_manager.MenuManager")
        mock_choice_main_menu = MockMenuManager.return_value.choice_main_menu

        auth_and_perms = login_manager.AuthenticationAndPermissions()
        auth_and_perms.check_password()

        # -tc- On vérifie que create_token est appelé avec les bons arguments
        mock_create_token.assert_called_once_with("test_departement")
        # -tc- On vérifie que choice_main_menu est appelé une fois et sans args
        mock_choice_main_menu.assert_called_once()
        mock_choice_main_menu.assert_called_once_with()
