import random
import os

fileLocation = 'words.txt'
words = []
try:
    file = open(fileLocation, 'r')
    data = file.read()
    temp_words = data.split(',')
    for word in temp_words:
        new_word = word[1:-1]
        words.append(new_word)
except IOError:
    print("Invalid file type")
    #just a precaution to have at least few words
else:
    file.close()
print(words)
