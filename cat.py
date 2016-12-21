movieNames = []

while True:
    print('Enter name of a movie ' + str(len(movieNames)+1) + '(Or enter nothing to stop)')
    name = input()
    if name == '':
        break
    movieNames = movieNames + [name] #appending to the list

print('Movie names are')
for movie in movieNames:
    print(movie)
