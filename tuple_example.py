zoo = ('elephent','tiger','leopard')

new_zoo = ('zebra','monkey',zoo)

print("Number of cages in new zoo:", len(new_zoo))

print("All animals in the new zoo are", new_zoo)

print("All animals from old zoo are", new_zoo[2])

print("Last animal brought from old zee is", new_zoo[2][-1])
#removing the array item, that's why -1
print("Number of anilams in the new zoo", len(new_zoo) - 1 + len(zoo))
