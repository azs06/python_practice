shoping_list = []
def print_help():
    print("Enter items for your grocery list")
    print("Enter SHOW to view list items")
    print("Enter DONE to print items")
    print("Enter HELP to print items")
#end of function block

def show_list():
    for item in shoping_list:
        print(item)
#end of function block

def addto_list(item):
    shoping_list.append(item)
    print("Item added, currently {} items in the list".format(len(shoping_list)))
#end of function block

def shopping_list():
    print_help()
    while True:
        new_item = input("> ")
        if new_item == "DONE":
            break
        elif new_item == "SHOW":
            shopping_list()
            continue
        elif new_item == "HELP":
            print_help()
            continue
        else:
            addto_list(new_item)

    print(shoping_list)
#end of function block

shopping_list()