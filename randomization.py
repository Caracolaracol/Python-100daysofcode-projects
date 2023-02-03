import random


random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)
print(random_float * 5)


random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# offset
# the list data type has some more methods:
list.append(x) # add an item to the end of the list. Equivalent to a[len(a):] = [x]
