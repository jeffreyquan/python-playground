def unique_list(x):
  return list(set(x))

x = ["apple", "pear", "banana", "apple", "strawberries", "mango", "pear"]

print(unique_list(x)) # ['strawberries', 'pear', 'apple', 'mango', 'banana']
