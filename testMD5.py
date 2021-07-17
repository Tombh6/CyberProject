import hashlib

password = input("input the passworld to hash:\n")
print("\nMD5\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hashObj = hashlib.md5(setpass)
    guessPass = hashObj.hexdigest()
    print(guessPass)
