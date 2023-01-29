def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(n + cnt) % len(letters)]
        cnt += 1
    return key

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey
# The adversary do somehting bad
key = generate_key(3)
message = input("What is your secret?")
message = "I LOVE YOU"
cipher = encrypt(key, message)

dkey = get_decryption_key(key)

plain = encrypt(dkey, cipher)

print("You are secret is \"{}\"".format(cipher))

print("Decrypted secret is \"{}\"".format(plain))

# You have to decrypt the secret!!! (Brute Force)
"""
for i in range(26):
    dkey = generate_key(i)
    message = encrypt(dkey, cipher)
    print(message)
"""
"""
The security of Caesar Cipher is based on the following.
- By keeping the algorithm secret

Why does Caesar Cipher give us one of the most valuable lessons in security?
- Because security should not be based on keeping the algorithm secret.
"""
