import passlib.hash

salt = "8sFt66z7"

words = ["changeme", "123456", "password"]

for word in words:
    sha1_hash = passlib.hash.sha1_crypt.hash(word, salt=salt)
    sha256_hash = passlib.hash.sha256_crypt.hash(word, salt=salt)
    sha512_hash = passlib.hash.sha512_crypt.hash(word, salt=salt)
    
    print(f"Word: {word}")
    print(f"SHA-1 Hash: {sha1_hash}")
    print(f"SHA-256 Hash: {sha256_hash}")
    print(f"SHA-512 Hash: {sha512_hash}")
    print("-" * 30)
