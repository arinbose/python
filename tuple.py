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