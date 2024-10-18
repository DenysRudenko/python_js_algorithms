import secrets
import hashlib

# creating a random 16 byte salt
salt = secrets.token_hex(16)
print(f'My salt is : {salt}')

password = 'qwerty'

# concatenate pass with salt
salted_password = salt + password

# lets hash the pass with md5(we can use other methods such as PBKDF2)
hash_object = hashlib.md5(salted_password.encode())
hashed_password = hash_object.hexdigest()

print(f'Hashed password is {hashed_password}')
