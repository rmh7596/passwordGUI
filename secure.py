import rsa
publicKey, privateKey = rsa.newkeys(512)

def encrypt(password):
    secure_pass =  rsa.encrypt(password.encode(), publicKey)
    return secure_pass;

def decrypt(p):
    d = rsa.decrypt(p, privateKey).decode()
    return d

def main():
    h = "Hello"
    h_e = encrypt(h)
    print(h)
    print(h_e)
    print(decrypt(h_e))

if __name__ == "__main__":
    main()
