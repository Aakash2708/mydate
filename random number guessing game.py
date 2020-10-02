import random

flag = True
while flag:
    num = input('Type a number for upper bound ; ')

    if num.isdigit():
        print('lets play the game')
        num = int(num)
        flag = False
    else:
        print('invalid input print again')

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    guess = input('plz enter a number b/w 1 and' + str(num) + ': ')
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print('BOOYAH')
    else:
        print('better luck next timr')
        count += 1

print('it took to', count, 'guess')

