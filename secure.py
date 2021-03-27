import rsa
publicKey, privateKey = rsa.newkeys(512)

def encrypt(password, key):
    secure_pass =  rsa.encrypt(password.encode(), key)
    return secure_pass;

def decrypt(p, key):
    d = rsa.decrypt(p, key).decode()
    return d

def main():
    h = "Hello"
    h_e = encrypt(h)
    print(h)
    print(h_e)
    print(decrypt(h_e))

if __name__ == "__main__":
    main()
