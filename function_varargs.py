def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count
#end of function block

print(total(10,11,2,3, coke=100, chocolate=50))