x = 50

def func():
    global x

    print("x is", x)
    x = 2
    print("Changed global x to", x)
#end of function

func()
print("x is ",x)