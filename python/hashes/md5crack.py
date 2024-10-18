import hashlib

my_password = input('Please enter your password: ')

# hash the pass to md5
md5_hash_password = hashlib.md5(my_password.encode()).hexdigest()

password_file = 'rockyou.txt'

# lets read the file

with open(password_file, 'r', encoding="latin-1") as file:
    for password in file:
        # strip removes the whitespaces or newline chars
        password = password.strip()
        hash_object = hashlib.md5(password.encode())
        hashed_password = hash_object.hexdigest()

        # check if the hash pass match the given hash
        if hashed_password == md5_hash_password:
            print(f'Password found : {password}')
            break
    else: 
        print("Password not found in the list")