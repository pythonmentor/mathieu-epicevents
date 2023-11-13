from argon2 import PasswordHasher, exceptions


ph = PasswordHasher()
hash = ph.hash('password')
print(hash)
try:
    print(ph.verify(hash, "password"))
except :
    print("pas bon")

    
print("cquoi : ",check_needs_rehash(hash)
