'''
All your local variables and methods call associated data will be placed on the stack. For each
method call, one stack frame will be created, and local as well as method call relevant data will
be placed inside that stack frame. Once the method execution is completed, the stack frame will be
removed.
Recursion Error occurs when function is called in recursively infinitely

Out of Memory Error:
Memory errors are mostly dependent on your systems RAM and are related to Heap. If you have
large objects (or) referenced objects in memory, then you will see OutofMemoryError
'''
print('............Example1................')
''''''
try:
    a = 100 / 0
    print (a)
except ZeroDivisionError:
        print ("Zero Division Exception Raised." )
else:
    print ("Success, no error!")
print('............Example2................')
try:
    inp = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')

print('............Example3................')
try:
    import math
    print(math.exp(1000))
except OverflowError:
        print ("OverFlow Exception Raised.")
else:
    print ("Success, no error!")

print('............Example4................')

try:
    a = 100
    b = "DataCamp"
    assert a == b
except AssertionError:
        print ("Assertion Exception Raised.")
else:
    print ("Success, no error!")

print('............Example5................')
class Attributes(object):
    a = 2
    print (a)

try:
    object = Attributes()
    print (object.attribute)
except AttributeError:
    print ("Attribute Exception Raised.")

print('............Example6................')
try:
    a = {1:'a', 2:'b', 3:'c'}
    print (a[4])
except LookupError:
    print ("Key Error Exception Raised.")
else:
    print ("Success, no error!")

print('............Example7................')
try:
    a = ['a', 'b', 'c']
    print (a[4])
except LookupError:
    print ("Index Error Exception Raised, list index out of range")
else:
    print ("Success, no error!")

print('............Example8................')
try:
    print (ans)
except NameError:
    print ("NameError: name 'ans' is not defined")
else:
    print ("Success, no error!")

print('............Example9................')
try:
    a = 5
    b = "DataCamp"
    c = a + b
except TypeError:
    print ('TypeError Exception Raised')
else:
    print ('Success, no error!')

print('............Example10................')
try:
    print (float('DataCamp'))
except ValueError:
    print ('ValueError: could not convert string to float: \'DataCamp\'')
else:
    print ('Success, no error!')