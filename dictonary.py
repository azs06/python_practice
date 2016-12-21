spam = {'color': 'red','age': 42}

print(type(spam))

for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)

picnicItems = {'apple': 5, 'cups': 2}

print("I am bringing " + str(picnicItems.get('cups', 0)) + " cups.")
print("I am bringing " + str(picnicItems.get('eggs', 0)) + " eggs")