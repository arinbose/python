'''
1.When called, it returns an object (iterator) but does not start execution immediately.
2.Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
3.Once the function yields, the function is paused and the control is transferred to the caller.
4.Local variables and their states are remembered between successive calls.
5.Finally, when the function terminates, StopIteration is raised automatically on further calls.
'''
print('Example-1')
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

'''Note normal function local variables are destroyed but generator 
local variables are not destroyed when function yields'''
a = my_gen()
print(next(a))

print(next(a))

print(next(a))

print('Example-2')
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# Using for loop with yield
for item in my_gen():
    print(item)

print('Example-3')
'''list expression below'''
my_list = [1,3,6,10]
list_ = [x**2 for x in my_list]
'''generator expression below'''
'''generator expression did not produce the required result immediately,its on demand'''
generator = (x**2 for x in my_list)

print(list_) # returns all elements at once
print(generator) # returns generator object not elements, next function prints elements
'''
A normal function to return a sequence will create the entire sequence in memory before returning
the result. This is an overkill, if the number of items in the sequence is very large.

Generator implementation of such sequences is memory friendly and is preferred since it only 
produces one item at a time.
'''

