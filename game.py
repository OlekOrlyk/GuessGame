# Guess the number
from pythonrandom.randommessage import get_message
from pythonrandom.randommessage import get_winmessage
import random
def main():
    guessesTaken = 10
    print('Hello! What is your name?')
    myName = input()

    number = random.randint(1, 100)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')

    while True:

        if guessesTaken == 1:
            print("This is your last chance")
        else:
            print('You have ' + str(guessesTaken) + ' tries')

        guess = input()
        guess = int(guess)


        if guess < number:
            print('Your guess is too low. ' + get_message())

        if guess > number:
            print('Your guess is too high.' +get_message())

        if guess == number:
            print('Well! ' + get_winmessage())
            break


        guessesTaken -= 1
        if guessesTaken == 0:
            print("Idiot,cant even guess a number.Whar are you doing with your life?")
            break


main()
