'''A tuple is a collection of objects which ordered and immutable. Tuples are sequences,
just like lists.'''
'''The differences between tuples and lists are, the tuples cannot be changed unlike lists'''

print('............Example1...........')
'''accessing tuple'''
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: "+str(tup1[0]))
print("tup2[1:5]: "+str(tup2[1:5]))

print('............Example2...........')
'''tuple cannot be modified i.e updated but new created'''
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
tup3 = tup1 + tup2;
print('New tuple;'+str(tup3));

print('............Example3...........')
'''Removing individual tuple elements is not possible. '''


print('............Example4...........')
'''element to element comparison'''
tuple1 = (1,2,3)
tuple2 = (1,2,4)
print (tuple1 == tuple2)


print('............Example5...........')
'''Compare tuples with heterogeneous items'''
tuple1 = (1, 2, 3)
tuple2 = (1, 2, "6")
print( tuple1 == tuple2 )
'''false if both are different'''

print('............Example6...........')
'''Comparing first element'''
a=(5,4)
b=(1,6)
if (a>b):print("a is bigger")
else: print("b is bigger")

print('............Example7...........')
foo = (1, 2, 3)
bar = (4, 5, 6)
'''printing tuples paralelly'''
for (f, b) in zip(foo, bar):
    print("f: ", f, "; b: ", b)

print('............Example8...........')
'''Unpacking tuple'''
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z))

print('............Example9...........')
test_tup = (10, 4, 5, 6, 7)
print("The original tuple : " + str(test_tup))
res = (test_tup[0], test_tup[-1])
print("The front and rear element of tuple are : " + str(res))

print('............Example10...........')
from operator import itemgetter

# initialize tuple
test_tup = (10, 4, 5, 6, 7)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Accessing front and rear element of tuple
# using itemgetter()
res = itemgetter(0, -1)(test_tup)

# printing result
print("The front and rear element of tuple are : " + str(res))

print('............Example11...........')
'''replace N th element'''
test_list = [('gfg', 1), ('was', 2), ('best', 3)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing change record
repl_rec = ('is', 2)

# Initializing N
N = 1

# Replace tuple according to Nth tuple element
# Using loops + enumerate()
for key, val in enumerate(test_list):
    if val[N] == repl_rec[N]:
        test_list[key] = repl_rec
        break

# printing result
print("The tuple after replacement is : " + str(test_list))

print('............Example12...........')
# initializing tuple- # Nth column in Tuple Strings
test_tuple = ('GfG', 'for', 'Geeks')

# initializing N
N = 1

# printing original tuple
print("The original tuple : " + str(test_tuple))

# using list comprehsion
# Nth column in Tuple Strings
res = list(sub[N] for sub in test_tuple)

# print result
print("The Nth index string character list : " + str(res))

print('............Example13...........')
# initialize list
test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 2

# Nth column Maximum in tuple list
# using list comprehension + max()
res = max([sub[N] for sub in test_list])

# printing result
print("Maximum of Nth Column of Tuple List : " + str(res))

from itertools import chain

# initializing tuple
test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using tuple() + chain.from_iterable()
res = tuple(chain.from_iterable(test_tuple))

# printing result
print("The flattened tuple : " + str(res))

print('...........Example13...........')
'''flatten list of tuple'''
from itertools import chain

# initializing tuple
test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using tuple() + chain.from_iterable()
res = tuple(chain.from_iterable(test_tuple))

# printing result
print("The flattened tuple : " + str(res))

print('...........Example14............')
'''flatten list of list another way'''
from itertools import chain

# initializing list of list
test_list = [[3, 5], [7, 3, 9], [1, 12]]

# printing original list of list
print("The original list : " + str(test_list))

# using itertools.chain() + sorted()
# sort flatten list of list
res = sorted(chain(*test_list))

# print result
print("The sorted and flattened list : " + str(res))

print('...........Example15............')
'''Unpacking nested tuples '''
# initialize list
test_list = [(4, (5, 'Gfg')), (7, (8, 6))]

# printing original list
print("The original list is : " + str(test_list))

# Unpacking nested tuples
# using list comprehension + * operator
res = [(z, *x) for z, x in test_list]

# printing result
print("The unpacked nested tuple list is : " + str(res))

print('...........Example16............')
'''Enumerate tuple-Unpacking tuple'''
for i,a in enumerate([4, 5, 6, 7]):
    print(i, ": ", a)

list = [('bob', 3), ('alice', 0), ('john', 5), ('chris', 4), ('alex', 2)]
print("Displaying Enumerated List")
for name, num in enumerate(list):
    print("{0}: {1}".format(name, num))

print('...........Example17............')
'''convert list into tuple'''
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = tuple(weekdays)
print(listAsTuple)

print('...........Example17............')
'''convert list into set'''
weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
listAsSet = set(weekdays)
print(listAsSet)

print('...........Example17............')
'''occurence of element in list'''
weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(weekdays.count('mon'))