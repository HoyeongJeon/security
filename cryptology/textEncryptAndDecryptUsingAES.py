import base64  # Base64 인코딩, 디코딩
from Crypto.Cipher import AES  #AES 암호화 모듈을 사용하기 위함
from Crypto.Util.Padding import pad, unpad  # AES 사용시 패딩과 언패딩을 하기 위해..



#padding 설정하기
Block_Size = 16

key = 'testkey'
plain_text = input('Tell me your secret: ')
print('Secret: ', plain_text)

cipher = AES.new(pad(key.encode(), Block_Size), AES.MODE_ECB)
msg = cipher.encrypt(pad(plain_text.encode(), Block_Size))

print('msg', msg)
m2 = base64.b64encode(msg)
print('base64 Encoded: ', m2)
decoded_msg = base64.b64decode(m2)
print('base64 Decoded: ', decoded_msg)

padded_plain = cipher.decrypt(decoded_msg)
unpadded_plain = unpad(padded_plain, Block_Size)
decoded_unpadded_plain = unpadded_plain.decode('utf-8')
print("Your Secret is {}".format(decoded_unpadded_plain))

