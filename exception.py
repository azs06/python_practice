try:
    count = int(input("Enter a number"))
except ValueError:
    print("That's not a number")
else:
    print("Hi "*count)