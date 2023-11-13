from argon2 import PasswordHasher, exceptions
from datetime import datetime, timezone, timedelta

import jwt
encoded_jwt = jwt.encode({"exp": datetime.now()+ timedelta(seconds=60), "department": "commercial"}, "secret", algorithm="HS256")
print("token : ", encoded_jwt)

jwt_decode = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])

print(jwt_decode['department'])
print(datetime.now()+ timedelta(seconds=60))




def verify_password(self, password):
    """
    Check if the password matches the hash
    Return Boolean
    """
    hashed_password = self.hash_password(password)
    try:
        if self.ph.verify(hashed_password, password):   
            engine = create_engine(f'mysql+pymysql://{self.username}:{hashed_password}@localhost/epic_events', echo=True)
        return self.ph.verify(hash, self.password)
    except:
        print("Your username or password is invalid")


# L’attribut echo=True oblige SQLAlchemy à enregistrer toutes les commandes SQL qu’il exécute
engine = create_engine(f'mysql+pymysql://root:{password}@localhost/epic_events', echo=True)
conn = engine.connect()


personnes = session.query(Personne). \
        filter(Personne.âge >= 20, Personne.âge <= 40). \
        order_by(Personne.âge.desc(), Personne.nom.asc(), Personne.prénom.asc())

if session:
        session.close()