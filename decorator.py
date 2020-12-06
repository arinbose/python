'''@ symbol is a syntactic sugar python provides to utilize decorator,'''
'''Put it simple decorator allow you to modify a given function's 
definition without touch its innermost (it's closure).'''
'''We have two different kinds of decorators in Python:

    Function decorators
    Class decorators
'''


'''https://www.datacamp.com/community/tutorials/decorators-python'''
print('.............Example1............')
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())

'''Rather than calling above way we can call like below with @uppercase_decorator
where uppercase_decorator is fn name where its passed'''
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())

print('.............Example2............')
'''Applying Multiple Decorators to a Single Function'''
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

'''Upper Case and Split Together'''
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())


print('.............Example3............')
'''Accepting Arguments in Decorator Functions'''
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")

'''Decorators have several use cases such as:
    Authorization in Python frameworks such as Flask and Django
    Logging
    Measuring execution time
    Synchronization
'''