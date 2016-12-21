number = 23
running = True

while running:
    guess = int(input("Enter an integer:"))

    if guess == number:
        print("You guessed it right")
        running = False
    elif guess < number:
        print("Number is a bit higher then what you guessed")
        running = False
    else:
        print("You guessed it higher then the number")
        running = False

else:
    print("The while loop is over now")
print("Done looping")
