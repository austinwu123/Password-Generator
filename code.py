import string

import random

characters = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_lowercase + string.ascii_uppercase)

digits = int(input("What is the number of characters you want to have in your password? "))

if digits <= 0:
    print("You must choose an answer bigger than 1")

else:
    print("Your Password Is: ", end="")
    for i in range(digits):
        print(random.choice(characters), end="")

