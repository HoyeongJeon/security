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
cipher = encrypt(key, message)

dkey = get_decryption_key(key)

plain = encrypt(dkey, cipher)

print("You are secret is \"{}\"".format(cipher))

print("Decrypted secret is \"{}\"".format(plain))

"""
# How to attack the cipher?
for i in range(26):
    dkey = generate_key(i)
    message = encrypt(dkey, cipher)
    print(message)
"""
