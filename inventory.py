stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v

    print("Total number of items: " + str(item_total))

#displayInventory(stuff)
def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin','dagger','gold coin', 'gold coin', 'ruby']
count = {}
z = {}
for item in dragonLoot:
    count.setdefault(item, 0)
    count[item] = count[item] + 1
z = count.copy()
z.update(inv)
print(z)

c = {x: inv.get(x, 0) + count.get(x, 0) for x in set(inv).union(count)}
print(c)

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
          inventory.setdefault(addedItems[i],0)
          inventory[addedItems[i]]=inventory[addedItems[i]]+1
    return inventory
