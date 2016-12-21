list = ["a","b","c","d"]

def loopy(items):
    # Code goes here
    for item in items:
        if item[0] == "a":
            continue
        else:
            print(item)

loopy(list)