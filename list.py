'''
The most basic data structure in Python is the sequence.
Python has six built-in types of sequences, but the most common ones are lists and tuples,
'''
list1 = [1, 3, 5, 7, 9]

print('............Example1...........')
for i in list1:
    print('List Values:' + str(i))

print('............Example2...........')
'''Finding length of list'''
length = len(list1)
print('List Length:' + str(length))

i = 0

print('............Example3...........')
'''Iterate list using while loop'''
while i < length:
    print('Iterate using while loop:' + str(list1[i]))
    i += 1

print('............Example4...........')
'''List comprehension'''
[print('List comprehension ->' + str(i)) for i in list1]

print('............Example5...........')
'''index and value using enumerate'''
for i, val in enumerate(list1):
    print('List Index->' + str(i) + " List Value->" + str(val))

print('............Example6...........')
import itertools

'''zip with for comprehension'''
num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]
for (a, b, c) in zip(num, color, value):
    print(a, b, c)

print('............Example7...........')
import itertools

num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

'''if all elements not having equal length then None printed'''
for (a, b, c) in itertools.zip_longest(num, color, value):
    print(a, b, c)

print('............Example8...........')
import itertools

num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256]

# Specifying default value as -1
for (a, b, c) in itertools.zip_longest(num, color, value, fillvalue=-1):
    print(a, b, c)

print('............Example9...........')


def countList(lst):
    return len(lst)


# Driver code
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print('Counting list of list element:' + str(countList(lst)))

print('............Example10...........')
'''Method1:-List to nested list conversion'''


def nestedlist(lst):
    res_list = []
    for element in lst:
        sub = element.split(', ')
        res_list.append(sub)
    return (res_list)


list4 = ['arin', 'bose', 'lets', 'try', 'python']

print(nestedlist(list4))

'''Method2:-List to nested list conversion'''


def extractDigits(lst):
    return [[el] for el in lst]


lst = ['alice', 'bob', 'cara']
print(extractDigits(lst))

print('............Example10A...........')
'''flatten a nested list'''
t =[[1,2,3],[6,7],[1010,5853]]
flat_list = []
for sublist in t:
    for item in sublist:
        flat_list.append(item)
print(flat_list)

print('............Example10B...........')
'''flatten nested list to list another way'''
from functools import reduce
l = [[1,2,3],[4,5,6], [7], [8,9]]
print(reduce(lambda x,y: x+y,l))

print('............Example10C...........')
'''flatten any nesting in python list'''
def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item

print(list(flatten([[[1, 2, 3], [4, 5]], 6])))

print('............Example11...........')
test_list = [["g", "o", "d"], ["i", "s"], ["g", "r", "e", "a", "t"]]
print("Original list is:" + str(test_list))

res = [''.join(ele) for ele in test_list]
print('String list is' + str(res))

print('............Example12...........')
'''convert-lists-into-similar-key-value-lists'''
test_list1 = [5, 6, 6, 4, 5, 6]
test_list2 = [8, 3, 2, 9, 10, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# creating a mesh of keys with empty values list
res = {key: [] for key in test_list1}

# loop to iterate through keys and values
for key, val in zip(test_list1, test_list2):
    res[key].append(val)

# printing result
print("The mapped dictionary : " + str(res))

print('............Example13...........')
'''joining list value to form a single string'''
sentence = ['this', 'is', 'a', 'sentence']
print('-'.join(sentence))

print('............Example14...........')
'''Accessing Values in Lists'''
list2 = [1, 2, 3, 4, 5, 6, 7];
print("Original List", list2)
print("list2[1:5]: ", list2[1:5])

print('............Example15...........')
'''Updating a list'''
list = ['physics', 'chemistry', 1997, 2000];
list[2] = 2001;
print("New value available at index 2 : " + str(list[2]))

print('............Example16...........')
'''delete from a list'''
list1 = ['physics', 'chemistry', 1997, 2000];
print('Original list' + str(list1));
del list1[2];
print("After deleting value at index 2 : " + str(list1))

print('............Example16...........')
'''appending list'''
aList = [123, 'xyz', 'zara', 'abc'];
aList.append(2009);
print("Updated List : " + str(aList))

print('............Example16...........')
'''extend in list'''
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print("Extended List : " + str(aList))

print('............Example16A...........')
'''append adds an element to a list, and extend concatenates the first list with another list '''
'''append adds its argument as a single element to the end of a list. The length of the list
itself will increase by one.
extend iterates over its argument adding each element to the list, extending the list. The
length of the list will increase by however many elements were in the iterable argument'''
'''Append has constant time complexity, O(1). 
   Extend has time complexity, O(k). '''
li = ['a', 'b', 'mpilgrim', 'z', 'example']
print(li)
li.append("new")
print(li)
li.append(["new", 2])
print(li)
li.insert(2, "new")
print(li)
li.extend(["two", "elements"])
print(li)
'''https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend?rq=1'''
print('............Example17...........')
'''insert in specific position in list'''
aList = [123, 'xyz', 'zara', 'abc']
aList.insert(3, 2009)
print('Final List After Insert: ' + str(aList))

print('............Example18...........')
'''pop method in list'''
aList = [123, 'xyz', 'zara', 'abc']
print("A List : " + str(aList.pop()))
print("B List : " + str(aList.pop(2)))
print("After pop list becomes" + str(aList))

print('............Example19...........')
'''remove method in list'''
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.remove('xyz');
print("List after remove method: " + str(aList))

print('............Example20...........')
'''reversed list'''
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.reverse();
print("Reversed List : " + str(aList))

print('............Example21...........')
'''removing elements from list using condn and loop'''
alist = ['good', 'bad', 'notgood', 'ajoba', 'bogulo']
i = 0
for x in alist[:]:
    if x == 'bad':
        alist.pop(i)
        i -= 1
    print('Inside->'+str(alist))
    i += 1
print(alist)

print('............Example22...........')
'''deleting item from list using enumerate-this is better as it breaks out'''
lst =[1,4,5,7,8,3]
for i, item in enumerate(lst):
    if item % 4 == 0:
        del lst[i]
        break
print((lst))

print('............Example23...........')
'''another way printing tuples'''
for num, cheese, color in zip([1,2,3], ['manchego', 'stilton', 'brie'],
                              ['red', 'blue', 'green']):
    print('{} {} {}'.format(num, color, cheese))

print('............Example24...........')
'''zip and join '''
a = ['foo1', 'foo2', 'foo3']
b = ['bar1', 'bar2', 'bar3']
'''print('printing zip:'+str(list(zip(a,b))))'''

print('printing join with zip: '+str([' '.join((a, b)) for a, b in zip(a, b)]))

print('printing join with zip printing next line: '+str('\n'.join(' '.join(x) for x in zip(a, b))))


print('............Example25...........')
'''searching element in list and printing index-enumerate searches multiple occurence'''
print('Index of element searched:'+str([index for index, j in enumerate(['foo', 'bar', 'baz', 'bar']) if j == 'bar']))

print('............Example26...........')
mylist =[1,2,3,4,5]
my_new_list=mylist
'''Below is process to create new list so that it doesnt point to old location using copy method'''
new_list = mylist.copy()
mylist[1]=100
'''Both values same as no new list create both point to same location'''
print('My new list'+str(my_new_list))
print('My old list'+str(mylist))
'''Below is process to create new list so that it doesnt point to old location'''
print('New List'+str(new_list))

print('............Example27...........')
'''Finding count of each element in list'''
from collections import Counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(z))
'''Finding specific element count'''
l = ["a","b","b"]
print("Count of b is :"+str(l.count("b")))

print('............Example28...........')
'''Unique value from list by converting list to set'''
mylist = ['nowplaying', 'PBS', 'PBS', 'nowplaying', 'job', 'debate', 'thenandnow']
myset = set(mylist)
print(myset)

print('............Example29...........')
'''arguments in python pass as string hence list also passed as string while passing as input'''
'''we are passing list as input here '''
import ast
import sys

list1 = ast.literal_eval(sys.argv[1])
list2 = ast.literal_eval(sys.argv[2])

print(list1)
print(list2)

print('............Example30...........')
'''list as input- pass like  1 2 3'''
input_string = input("Enter a list elements separated by space ")

print("\n")
userList = input_string.split()
print("user list is ", userList)
# Calculating the sum of input list elements
sum1 = 0
for num in userList:
    sum1 += int(num)
print("Sum = ", sum1)


print('............Example31...........')
'''passing list length and list value- pass size liek 2 then enter value for each like 1 then 2'''
numberList = []
n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)


print('............Example32...........')
'''passing nested list'''
'''listLen = int(input("Enter the number of sublist "))

print("\n")
finalList = [[int(input("Enter number: ")) for _ in range(listLen)] for _ in range(listLen)]
print("List is")
print(finalList)'''


print('............Example33...........')
'''Unpacking list-while passing we do not mention number of arguments'''
def fun(a, b, c, d):
    print(a, b, c, d)

# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)

print('............Example34...........')
'''This function uses packing to sum
   unknown number of arguments '''
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

'''1. Used in socket programming to send a vast number of requests to a server.
2. Used in Django framework to send variable arguments to view functions.
3. There are wrapper functions that require us to pass in variable arguments.
4. Modification of arguments become easy, but at the same time validation is not proper, so they must be used with care. '''

print('............Example35...........')
'''sort flatten list of list  '''
# initializing list of list
test_list = [[3, 5], [7, 3, 9], [1, 12]]

# printing original list of list
print("The original list : " + str(test_list))

# using sorted + list comprehension
# sort flatten list of list
res = sorted([j for i in test_list for j in i])

# print result
print("The sorted and flattened list : " + str(res))