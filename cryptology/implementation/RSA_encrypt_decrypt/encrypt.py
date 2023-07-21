"""
파일 암호화 하는 함수!
인자 
1. message file 경로
2. public key 경로

암호화 할 파일 읽기
임시키(대칭키) 생성
임시키로 파일 암호화
암호화 파일 생성 ( 암호화된 임시키 + 넌스 + 태그 + 암호화된 파일 내용)
파일 암호화 방식은 GCM 모드를 사용할 예정(무결성 체크)

"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import os


def encrypt(targetFilePath, publicKeyPath):
    # 타겟 파일의 데이터 읽기!
    with open(targetFilePath, "rb") as f:
        data = f.read()
    data = bytes(data)

    # publicKey.pemd에서 key 읽어옴
    with open(publicKeyPath, "rb") as f:
        public_key = f.read()

    # public key 추출
    key = RSA.import_key(public_key)

    # 파일 내용 암호화 할 session key 생성
    session_key = os.urandom(16)

    # session key 암호화를 위해 rsa key 암호화 모듈 생성 (PKCS1)
    cipher = PKCS1_OAEP.new(key)
    encrypted_session_key = cipher.encrypt(session_key)

    # GCM 모드 암호화를 위한 12바이트 넌스 생성
    nonce = os.urandom(12)
    cipher = AES.new(session_key, AES.MODE_GCM, nonce)

    # 암호화!
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open("encrypted_file.txt", "wb") as f:
        [f.write(x) for x in (encrypted_session_key, nonce, tag, ciphertext)]

    print("ENCRYPT DONE.")


encrypt(
    "/Users/hoyoungjeon/Documents/cryptography_by_python/hello.txt",
    "/Users/hoyoungjeon/Documents/cryptography_by_python/public.pem",
)
