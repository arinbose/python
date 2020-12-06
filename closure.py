print('.....Example1....')
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
'''
Closures can avoid the use of global values and provides some form of data hiding. It can also 
provide an object oriented solution to the problem.
When there are few methods (one method in most cases) to be implemented in a class, closures can 
provide an alternate and more elegant solution. But when the number of attributes and methods get 
larger, it's better to implement a class.
'''
print('........Example2.........')

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Output: 27
print(times3(9))

'''All function objects have a __closure__ attribute that returns
a tuple of cell objects if it is a closure function.'''
make_multiplier_of.__closure__
print(times3.__closure__)
print(times3.__closure__[0].cell_contents)
