""" 
Decrypt the encrypted file!
암호화의 역순

"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES


def decrypt(encryptedFilePath, privateKeyPath):
    # privateKey.pem에서 key 읽어옴
    with open(privateKeyPath, "rb") as f:
        private_key = f.read()

        # private key 추출
        key = RSA.import_key(private_key)

    # 복호화에 필요한 파라미터 추출
    with open(encryptedFilePath, "rb") as f:
        encrypted_session_key, nonce, tag, ciphertext = [
            f.read(x) for x in (key.size_in_bytes(), 12, 16, -1)
        ]

    # 세션 키 복호화를 위한 RSA 모듈 생성
    cipher = PKCS1_OAEP.new(key)
    session_key = cipher.decrypt(encrypted_session_key)

    # 암호화된 파일 복호화를 위한 AES 모듈 생성
    cipher = AES.new(session_key, AES.MODE_GCM, nonce)

    # 복호화
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

    # 복호화 파일 저장!
    with open("decrypted_file.txt", "wb") as f:
        f.write(decrypted_data)

    print("DECRYPT DONE.")


decrypt(
    "/Users/hoyoungjeon/Documents/cryptography_by_python/encrypted_file.txt",
    "/Users/hoyoungjeon/Documents/cryptography_by_python/private.pem",
)
