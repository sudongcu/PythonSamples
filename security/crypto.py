#pip install pycryptodome
from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode

key = b'dgseo123456dgseo'

class AESCrypto:

    def init(self):
        pass

    def Encrypt(self, data):
        aes = AES.new(key, AES.MODE_EAX)
        nonce = aes.nonce
        encdata, tag = aes.encrypt_and_digest(data.encode())
        return b64encode(encdata), b64encode(tag), b64encode(nonce)

    def Decrypt(self, encdata, tag, nonce):
        encdata = b64decode(encdata)
        tag = b64decode(tag)
        nonce = b64decode(nonce)

        aes = AES.new(key, AES.MODE_EAX, nonce)
        decdata = aes.decrypt_and_verify(encdata, tag)
        return decdata.decode('utf-8')

testdata = 'dgseo is totally fine. 123456789'

a = AESCrypto()

encdata = a.Encrypt(testdata)
print(encdata)

decdata = a.Decrypt(encdata[0], encdata[1], encdata[2])
print(decdata)