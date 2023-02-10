import random # 실제 암호를 위해 사용하려면, random 모듈이 아닌 secret 모듈을 사용해야함.

def generate_key():
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    for c in letters:
        random_num = random.randint(0,len(cletters) - 1)
        key[c] = cletters.pop(random_num)
    return key

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

key = generate_key()
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)