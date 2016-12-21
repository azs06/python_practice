import random

start = 5


def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2


while start:
    random_num = random.randint(1, 99)

    if even_odd(random_num):
        print("{} is even".format(random_num))
    else:
        print("{} is odd".format(random_num))

    start = start - 1
