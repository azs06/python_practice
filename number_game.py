import random


def game():
    random_number = random.randint(1, 10)
    guesses = []
    while len(guesses) < 5:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("That's not a number")
        else:
            if guess == random_number:
                print("You guessed it correctly, the number is  {}".format(random_number))
                break
            elif guess > random_number:
                print("too high, You missed")
            else:
                print("too low, You missed")
            guesses.append(guess)

    else:
        print("all out of guess!, the number was {}".format(random_number))
        play_again = input("do you want to play again Y/N ")
        if play_again.lower() == 'n':
            print("Bye!")
        elif play_again.lower() == 'y':
            print("starting game again..")
            game()


game()
