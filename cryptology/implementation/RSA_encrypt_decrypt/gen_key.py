"""
RSA Key 쌍 생성 (2048)
"""
from Crypto.PublicKey import RSA

# 2048 바이트 RSA 키 생성
key = RSA.generate(2048)

# 개인키 추출
private_key = key.export_key()

# 공개키 추출
public_key = key.publickey().export_key()

with open("private.pem", "wb") as f:
    f.write(private_key)

with open("public.pem", "wb") as f:
    f.write(public_key)

print("Key generated.")
print("DONE")
