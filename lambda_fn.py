print('............Example1..........')
lambda_cube = lambda y: y * y * y
print('Lambda Fn:' + str(lambda_cube(5)))

print('............Example2..........')
li = [5, 7, 22, 97, 54, 62, 77, 23, 73]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print('Using lambda() Function with filter():' + str(final_list))

print('............Example3..........')
'''map takes a fn and list as inputs'''
li = [5, 7, 22, 97, 54, 62, 77, 23, 73]
final_list = list(map(lambda x: x * 2, li))
print('Using lambda() Function with map():' + str(final_list))

print('............Example4..........')
from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print('Using lambda() Function with reduce():' + str(sum))

print('............Example5..........')
A = [-1, 3, 7, 99, 0]
print('max using lambda and reduce'+str(reduce(lambda x, y : x if x > y else y,A)))

print('............Example6..........')
scores = [("Jade",21),("Rab",110),("Sylvando",39),("Erik",19)]
scores.sort(key=lambda t: t[1])
print('Sorting complex type using lambda'+str(scores))