import itertools
import string
import hashlib


def guess_password(real):
    chars = string.ascii_lowercase + string.digits #a-z + 0-9
    chars1 = string.ascii_uppercase + string.digits # A-Z 0-9
    chars2 = string.ascii_letters + string.digits # A-Z, a-z 0-9
    chars4 = string.ascii_uppercase
    chars5 = string.ascii_lowercase

    attempts = 0
    for password_length in range(1, 6):
        for guess in itertools.product(chars4, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            hashCode = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()

            if hashCode == real:
                print("Password is: " + guess)
                print (int(attempts))
                quit()


print(guess_password('4c462d6dd59d782386bb1cdad0060c70'))
