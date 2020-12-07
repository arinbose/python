'''
Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value
pair.
'''
print('.........Example1.........')
person_dict ={'name':"Trey",'company':"Truthful Tech LLC"}
for key ,value in  person_dict.items():
    print(f"Key {key} has value {value}")

print('.........Example2.........')
my_dict = {'name': 'Jack', 'age': 26}
# update dictionary value
my_dict['age'] = 27
print(my_dict)

# add item
my_dict['address'] = 'Downtown'
print(my_dict)

print('.........Example3.........')
# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))
print(squares)  #{1: 1, 2: 4, 3: 9, 5: 25}

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

#print(squares) # this will give error

print('.........Example4.........')
# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

print(squares)

print('.........Example5.........')
# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}

print(odd_squares)

print('.........Example6.........')
#Dictionary Membership Test
# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# membership tests for key only not value
# Output: False
print(49 in squares)

print('.........Example7.........')
'''Iterating through Dictionary'''
# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])