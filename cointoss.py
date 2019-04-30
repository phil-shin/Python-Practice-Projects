# cointoss.py
# Coin toss game

import random, logging
logging.disable()
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()
    logging.debug(guess)
randomNum = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug(randomNum)
if randomNum == 0:
    toss = 'tails'
else:
    toss = 'heads'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        
logging.debug('End of program')
