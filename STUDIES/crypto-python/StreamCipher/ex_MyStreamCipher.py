import random


class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return (self.rand()//2**23) % 256


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


'''
header.encode(), cipher.
header.encode() 동일하기에, header.encode()와 cipher를 xor한 값이 bruteforce 한 값과 같아야 함!
'''


def brute_force(plain, cipher):
    # insert code here
    for key in range(2**31):
        bf_key = KeyStream(key)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
        else:
            return key
    return False


    # This is Alice
secret_key = random.randrange(2**20)
print(secret_key)
key = KeyStream(secret_key)
header = "MESSAGE: "
message = header + "My secret message to Bob"
message = message.encode()
cipher = encrypt(key, message)

# This is Bob
key = KeyStream(secret_key)
message = encrypt(key, cipher)
print(message)

# This is Eve
bf_key = brute_force(header.encode(), cipher)
print("Eve's brute force key:", bf_key)
key = KeyStream(bf_key)
message = encrypt(key, cipher)
print(message)
