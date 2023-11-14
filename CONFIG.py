import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


config = configparser.ConfigParser()
config.read('config.ini')  
config_root = config["root"]
password = config_root["password"]
config_jwt = config["jwt"]
SECRET = config_jwt["secret"]
ENGINE = create_engine(f'mysql+pymysql://root:{password}@localhost/epic_events', echo=True)
Session = sessionmaker(bind=ENGINE)
SESSION = Session()