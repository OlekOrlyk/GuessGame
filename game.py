# Guess the number
from pythonrandom.randommessage import *

import random


def main():
    records = get_record_list()
    if len(records):
        print("Champions")
        print_records(records)
        print("Hello!Can you beat them?")
    else:
        print("Hello!?")

    guessesTaken = 10
    print('What is your name?')
    my_name = input()

    number = 10
    # random.randint(1, 100)
    print('Well, ' + my_name + ', I am thinking of a number between 1 and 100.')

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
            print('Your guess is too high.' + get_message())

        if guess == number:
            champion = get_champion(records)
            is_your_record = save_record(records, my_name, guessesTaken)
            if champion["score"]:
                if champion["score"] < guessesTaken:
                    if champion["name"] == my_name:
                        print("You beat yourself,congratulations!")
                    else:
                        print("You beat " + champion["name"])
                else:
                    if is_your_record:
                        print("You only beat yourself!Shame on you.")
                    else:
                        print('Well! ' + get_winmessage())

            else:
                print("You set the first record!")
            break

        guessesTaken -= 1
        if guessesTaken == 0:
            print("Idiot,cant even guess a number.Whar are you doing with your life?")
            break


main()
