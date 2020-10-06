import random
import string

def random_pswd (pswdlen = 10):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(pswdlen))
print('your random pasword is :',random_pswd( ))