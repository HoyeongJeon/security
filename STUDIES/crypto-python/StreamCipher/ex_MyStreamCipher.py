
class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        # 아무리 숫자가 커도 2**31로 mod 연산을 하므로 maximum 31bits!
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256


def get_key(message, cipher):
    # insert code here
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])


def crack(key_stream, cipher):
    # insert code here
    length = min(len(key_stream), len(cipher))
    return bytes([cipher[i] ^ key_stream[i] for i in range(length)])


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


def modification(cipher):
    # insert code here
    modified_cipher = [0] * len(cipher)
    modified_cipher[10] = ord(' ') ^ ord('1')
    modified_cipher[11] = ord(' ') ^ ord('0')
    modified_cipher[12] = ord('1') ^ ord('0')
    return bytes([modified_cipher[i] ^ cipher[i] for i in range(len(cipher))])


# This is the message that Eve gives Alice
message = "This is my long message that Eve tricks Alice into using".encode()


'''
key 재설정이유! 
- 사용할 key의 시작지점을 갖게해주기 위함!
'''

# This is Alice
key = KeyStream(10)
cipher = encrypt(key, message)

# This is Eve getting the key stream
eves_key_stream = get_key(message, cipher)

# This is Bob
key = KeyStream(10)
message = encrypt(key, cipher)

# This is Alice sending a new message
message = "Hey Bob. Let's take over the world domination.".encode()
key = KeyStream(10)
cipher = encrypt(key, message)

# This is Eve extracting the message
eves_decryption = crack(eves_key_stream, cipher)
print(eves_decryption)
