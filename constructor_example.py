class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
'''print(num1.attr)'''

'''Deleting Attributes and Objects'''
num1 = ComplexNumber(2,3)
del num1.imag
'''
print(num1.get_data())
OUTPUT:AttributeError: 'ComplexNumber' object has no attribute 'imag'
'''
del ComplexNumber.get_data
'''
num1.get_data()
AttributeError: 'ComplexNumber' object has no attribute 'get_data'
'''
c1 = ComplexNumber(1,3)
'''deleting object below
On the command del c1, this binding is removed and the name c1 is deleted from the corresponding 
namespace. The object however continues to exist in memory and if no other name is bound to it,
it is later automatically destroyed.
'''
del c1
'''
print(c1)
NameError: name 'c1' is not defined
'''

