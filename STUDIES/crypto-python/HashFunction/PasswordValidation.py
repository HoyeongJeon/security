import hashlib
import base64


iterations = 45454
salt_alice = "".encode()
password_alice = "password".encode()
value_alice = base64.b64encode(hashlib.pbkdf2_hmac(
    "sha512", password_alice, salt_alice, iterations, dklen=128))
print(value_alice, salt_alice, iterations)

salt_bob = "dslfajdfadsjf23j41234jdlkfnclvknqs;dlkfj12;3".encode()
password_bob = "password".encode()
value_bob = base64.b64encode(hashlib.pbkdf2_hmac(
    "sha512", password_bob, salt_bob, iterations, dklen=128))
print(value_bob, salt_bob, iterations)
