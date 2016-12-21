print("hello world")
some_variable = 10
hello_world = "This is a string"
#so cool, I don't have to use semicolon? if not careful, could cause problem

single_quote = 'he\'s wrong!'

print(single_quote)

triple_quote = """hello I can put anything here"""

print(triple_quote)

print(str(5))

status_message = "I want to eat {} {}"

print(status_message.format(5, "mangoes"))
print(status_message.format(1, "banana","test"))

list = [1,2,3]
list.extend([4,5,6])
print(list)
list.append([7,9])
print(list)
list.remove([7,9])
print(list)