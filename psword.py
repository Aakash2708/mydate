import random
import string
n =  int(input('enter the value of password :'))
def random_pswd (pswdlen = n):
    letters = string.ascii_uppercase
    words = string.ascii_lowercase
    numbers = string.digits
    special_chr = string.punctuation
    password = []
    password.extend(list(letters))
    password.extend(list(numbers))
    password.extend(list(words))
    password.extend(list(special_chr))
    return ''.join(random.choice(password) for i in range(pswdlen))
print('your random pasword is :',random_pswd( ))