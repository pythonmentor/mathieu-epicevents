from controllers.login_manager import AuthenticationAndPermissions
from views.login import ViewLogin
from models.event import Event
from settings import Base, ENGINE

def main():
    Base.metadata.create_all(ENGINE)
    run = AuthenticationAndPermissions()
    run.check_password()


if __name__ == "__main__":
    main()

