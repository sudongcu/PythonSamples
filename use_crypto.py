from security.crypto import AESCrypto

testdata = 'dgseo is totally fine. 123456789'

a = AESCrypto()

encdata = a.Encrypt(testdata)
print(encdata)

decdata = a.Decrypt(encdata[0], encdata[1], encdata[2])
print(decdata)