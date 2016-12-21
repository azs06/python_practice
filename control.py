number = 23
guess = int(input('Enter an integer:'))

if number == guess:
    print('You guessed it right')
elif number > guess:
    print('Number is higher then guess ')
else:
    print("No, it's a little lower then that.")
print("I will be printed any way")
