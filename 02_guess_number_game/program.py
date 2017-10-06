import random

print('-------------------------------')
print('Guess That Number Game')
print('-------------------------------')

the_number = random.randint(1, 100)

guess = -1

name = input('What is your name? ')
while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:

        print('Sorry {1} your guess of {0} was too high'.format(guess, name))
    else:
        print('Correct')

print('Done')
