'''
A set is an unordered collection of items. Every set element is unique (no duplicates) and must be
immutable (cannot be changed).
A set itself is mutable. We can add or remove items from it.
'''
print('..........Example1..........')
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

print('..........Example2..........')
# we can make set from a list
# Output: {1, 2, 3} i.e prints distinct value as its set
my_set = set([1, 2, 3, 2])
print(my_set)

print('..........Example3..........')
# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.
try:
    my_set = {1, 2, [3, 4]}
except Exception as e: print(e) # error we get unhashable type: 'list'

print('..........Example4..........')
'''
Sets are mutable. However, since they are unordered, indexing has no meaning.
We cannot access or change an element of a set using indexing or slicing. Set data type does not 
support it.
We can add a single element using the add() method, and multiple elements using the update() 
method. The update() method can take tuples, lists, strings or other sets as its argument.
'''
# initialize my_set
my_set = {1, 3}
print(my_set)

'''set doesnt support index'''
try:
    my_set[0]
except Exception as e: print(e) # OUTPUT:'set' object is not subscriptable

print('..........Example5..........')
'''add element to set'''
my_set.add(2)
print(my_set)  # 1,2,3

print('..........Example6..........')
# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

print('..........Example7..........')
'''
# Difference between discard() and remove()
'''
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)


print('..........Example8..........')
# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)