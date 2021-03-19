import rsa
publicKey, privateKey = rsa.newkeys(512)
s = "Hello World"
e = rsa.encrypt(s.encode(), publicKey)
print("original string: ", s)
print("encrypted string: " , e)
d = rsa.decrypt(e, privateKey).decode()
print("decrypted string: ", d)
