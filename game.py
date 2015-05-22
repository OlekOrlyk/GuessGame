# Guess the number

import random

guessesTaken = 10
print('Hello! What is your name?')
myName = input()

number = random.randint(1, 100)
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')

while True:

    print('Take a guess.You have ' + str(guessesTaken) + ' tries')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        print('Congratulations!you are smarter than you think!')
        break
    if guessesTaken == 0:
        print("Idiot,cant even guess a number.Whar are you doing with your life?")
        break
    guessesTaken -= 1
