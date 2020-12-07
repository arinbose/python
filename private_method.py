# Python program to
# demonstrate private methods
'''Python uses ‘_’ symbol to determine the access control for a
specific data member or a member function of a class.'''
print('........Example1.......')
# Creating a Base class
class Base:

    # Declaring public method
    def fun(self):
        print("Public method")

    # Declaring private method
    def __fun(self):
        print("Private method")

    # Creating a derived class


class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)

    def call_public(self):
        # Calling public method of base class
        print("\nInside derived class")
        self.fun()  # Calling Base class

    def call_private(self):
        # Calling private method of base class
        self.__fun()

    # Driver code


obj1 = Base()

# Calling public method
obj1.fun()   # Public method

obj2 = Derived()
obj2.call_public()

# Uncommenting obj1.__fun() will
# raise an AttributeError

# Uncommenting obj2.call_private()
# will also raise an AttributeError

'''The above example shows that private methods of the class can neither be accessed outside
the class nor by any base class.'''

print('..........Example-2...........')
'''private methods can be accessed by calling the private methods via public methods.'''


class A:
    # Declaring public method
    def fun(self):
        print("Public method")

        # Declaring private method
    def __fun(self):
        print("Private method")

    # Calling private method via
    # another method
    def Help(self):
        self.fun()
        self.__fun()
    # Driver's code

obj = A()
obj.Help()

