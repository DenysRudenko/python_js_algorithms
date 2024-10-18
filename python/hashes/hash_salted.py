import hashlib

password = 'qwerty'
salt = '123123123123123'

# adding salt to simple plaintext password
salted_password = salt + password

# creating md5 has for our salted_password
md5_hash = hashlib.md5(salted_password.encode()).hexdigest()

print(salted_password)
print(f'My md5 hashed password with salt is = {md5_hash}')
