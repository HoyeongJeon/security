import hashlib


def modify(message):
    l = list(message)
    l[0] = l[0] ^ 1
    return bytes(l)


# These are Alice's RSA keys
# Public key (e,n): 5 170171
# Secret key (d) 9677
n = 170171
e = 5
d = 9677

message = "Bob you are awesome".encode()

sha256 = hashlib.sha256()
sha256.update(message)
h_alice = sha256.digest()
h_alice = int.from_bytes(h_alice, byteorder='big') % n
print("Hash value", h_alice)

sign = h_alice ** d % n  # Insert code here
print(message, sign)

# This is Eve being evil and modifies the message
message = modify(message)
print(message)

# Bob verifying the signature
sha256 = hashlib.sha256()
sha256.update(message)
h_bob = sha256.digest()
h_bob = int.from_bytes(h_bob, byteorder='big') % n

print("Hash value", h_bob)

verification = sign ** e % n
print("Verification value", verification)
