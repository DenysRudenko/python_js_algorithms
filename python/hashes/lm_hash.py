import passlib.hash

words = ["Napier", "Foxtrot"]


for word in words:
    lm_hash = passlib.hash.lmhash.hash(word)
    nt_hash = passlib.hash.nthash.hash(word)
    
    print(f"Word: {word}")
    print(f"LM Hash: {lm_hash}")
    print(f"NTLM Hash: {nt_hash}")
    print("-" * 30)
