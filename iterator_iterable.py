print('........Example1..........')
# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

#Iterate and print value
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

print('........Example2..........')
# Function to check object
# is iterable or not
def iterable(obj):
    try:
        iter(obj)
        return True

    except TypeError:
        return False


# Driver Code- Check object is iterable or not
for element in [34, [4, 5], (4, 5),
                {"a": 4}, "dfsdf", 4.5]:
    print(element, " is iterable : ", iterable(element))

print('........Example3..........')
'''iterating using loop'''
lst = [11, 22, 33, 44, 55]
iter_lst = iter(lst)
while True:
    try:
        print(iter_lst.__next__())
    except:
        break

print('........Example4..........')
'''Error Handling - StopIterationError'''
listB = ['Cat', 'Bat', 'Sat', 'Mat']
iter_listB = listB.__iter__()
try:
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__()) #StopIteration error
except:
    print(" \nThrowing 'StopIterationError'",
                     "I cannot count more.")

print('........Example5..........')

class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1

if __name__ == '__main__':
    a,b =2,5
    c1 = Counter(a,b)
    c2 = Counter(a,b)

    print("Print the range without iter()")
    for i in c1:
        print("Eating more pizza",i,end="\n")

    #Way2: using iter()
    obj = iter(c2)
    try:
        while True:
            print("Eating more Pizzas, couting ", next(obj))
    except:
        print("END OF LOOP")

print('........Example6..........')
'''islice(iterable, start, stop, step)
   starmap(func., tuple list) '''

import itertools
li = [2, 4, 5, 7, 8, 10, 20]
li1 = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ]

# using islice() to slice the list acc. to need
# starts printing from 2nd index till 6th skipping 2
print ("The sliced list values are : ",end="")
print (list(itertools.islice(li,1, 6, 2)))

# using starmap() for selection value acc. to function
# selects min of all tuple values
print ("The values acc. to function are : ",end="")
print (list(itertools.starmap(min,li1)))

print('........Example7..........')
mylist = [1, 2, 3]
for i in mylist:
    print(i)
'''mylist is iterable
Generators are iterators, a kind of iterable you can only iterate over once.
'''