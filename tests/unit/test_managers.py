import pytest
from tests import conftest
import jwt
from controllers.menu_manager import password, SECRET, algo, SESSION
from controllers.login_manager import AuthenticationAndPermissions
from views.login import ViewLogin
import views.login
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from argon2 import PasswordHasher, exceptions
from controllers.menu_manager import password, SECRET, algo, SESSION
from models.staff import Staff
import jwt
from datetime import datetime, timezone, timedelta
from models.client import Client, ClientRepository
from controllers.menu_manager import MenuManager
from views.menu import Menu
from views.login import ViewLogin


"""
class TestLogin:
    
    def test_check_password(self, mocker):
        def mockreturn_email():
            return "sarah@gmail.com"
        def mockreturn_password():
            return "essai"
        mocker.patch('views.login.ViewLogin.get_email', return_value="saah@gmail.com")
        mocker.patch('views.login.ViewLogin.get_password', return_value="essai")
        sut = AuthenticationAndPermissions()
        #menu_manager = MenuManager(session, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTk5NzI3ODUsImRlcGFydG1lbnQiOiJjb21tZXJjaWFsIn0.OGmsJtL_JUBLyd2Oy8pULBal2I7qqvCK2ZN5unWLnt8")
        sut.check_password()
        mock = mocker.patch('controllers.login_manager.AuthenticationAndPermissions.check_password',)
        mock.assert_called()
"""

class TestDisplayData:

    def test_display_all_table():
        
