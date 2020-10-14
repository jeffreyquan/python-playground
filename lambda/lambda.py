
from functools import reduce

f = lambda x, y: x + y
sum = f(1, 2)

print(sum) # 3

# map
a = [1, 2, 3, 4, 5]
multiples_of_two = map(lambda x: x * 2, a);

print(multiples_of_two) # [2, 4, 6, 8, 10]

# filter
b = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, b)

print(evens) # [2, 4, 6, 8]

# reduce
c = [8, 9, 2, 0, 11, 4, 3]
sum = reduce(lambda x, y: x + y, c)

print(sum) # 37
