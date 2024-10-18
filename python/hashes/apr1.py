import passlib.hash

salt = "Pkwj6gM4"

words = ["changeme", "123456", "password"]

for word in words:
    apr1_hash = passlib.hash.apr_md5_crypt.hash(word, salt=salt)
    
    print(f"Word: {word}")
    print(f"APR1 Hash: {apr1_hash}")
    print("-" * 30)
