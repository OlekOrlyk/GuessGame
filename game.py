# Guess the number

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
            print('Your guess is too high.' + get_message())

        if guess == number:
            print('Congratulations!you are smarter than you think!')
            break


        guessesTaken -= 1
        if guessesTaken == 0:
            print("Idiot,cant even guess a number.Whar are you doing with your life?")
            break

def get_message():
    list =["HAHA!","You will never do it!","Just stop it!","Its just a number how hard can it be?","Can you count untill 5?"]
    index=random.randint(0,4)
    return list[index]
main()
