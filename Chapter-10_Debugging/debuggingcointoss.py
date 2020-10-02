#! python3
# The code bellow has a few problems. Try to run the program, indentify what the problem(s) is(are) and change it to make it work properly. Don't forget to commit!!

import random



guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter "heads" or "tails"')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game...')
