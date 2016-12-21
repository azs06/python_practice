import random


def game():
    secret_number = 5
    guesses = []
    while len(guesses) < 5:
        guess = random.randint(1, 10)
        if guess == secret_number:
            print("Computer guessed it correctly, the number is  {}".format(secret_number))
            break
        elif guess > secret_number:
            print("too high, You missed, computer guessed {}".format(guess))
        else:
            print("too low, You missed, computer guessed {}".format(guess))
        guesses.append(guess)
    else:
        print("all out of guess!, the number was {}".format(secret_number))
        play_again = input("do you want to play again Y/N ")
        if play_again.lower() == 'n':
            print("Bye!")
        elif play_again.lower() == 'y':
            print("starting game again..")
            game()


game()
