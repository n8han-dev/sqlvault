
from cryptography.fernet import Fernet

key = b'FVfDjxEQGzuI6Si76sWbmN6Dh7wap_RZ7dwGj8Shois='
cs = Fernet(key)
'''
pasw = cs.encrypt(b"imApassword")

with open("somefile", "wb") as f:
    f.write(pasw)
'''

with open("somefile.bin", "rb") as f:
    for l in f:
        eps = l

dps = cs.decrypt(eps)
ps = input("enter password: ")
pps = bytes(dps).decode("utf-8")
if ps == pps:
    print('Correct!')
else:
    print("Incorrect!")

