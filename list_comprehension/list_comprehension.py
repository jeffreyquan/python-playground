letters = [letter for letter in 'comprehension']

print(letters) # ['c','o','m','p','r','e','h','e','n','s','i','o','n']

even_num_list = [x for x in range(10) if x % 2 == 0]

print(even_num_list) # [0, 2, 4, 6, 8]

num_list = [y for y in range(100) if y % 3 == 0 and y % 5 == 0]

print(num_list) # [0, 15 , 30, 45, 60, 75, 90]

names = "  Ben | John | Bob   | Cat  | Dog "
name_list = [x.strip() for x in names.split("|")]

print(name_list) # ['Ben', 'John', 'Bob', 'Cat', 'Dog']

def flat_list(lists):
  return [y for x in lists for y in x]

lists = [['cat', 'dog'], ['bird', 'lizard', 'tiger']]

new_flat_list = flat_list(lists)

print(new_flat_list) # ['cat', 'dog', 'bird', 'lizard', 'tiger']