import math as maths

# Exercise 1 - Operators
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

# Exercise 2 - Strings
print('Robin')
print('Australia')

# Exercise 3 - Types
print(type(10))
print(type(9.8))
print(type(4 - 4j))
print(type(['Robin', 'Australia']))
print(type('Robin'))

print(type(('yep', 20, False, 3.12)))
print(type({12.0,2.2,3.12,4.3}))
print(type({'name':'Robin', 'country':'Aus', 'skills':['pay_bills', 'electronics', 'comp_sys']}))

# Exercise 4 - Euclidean Distance
point_a = [2,3]
point_b = [10,8]
 
dist = maths.sqrt((point_b[1]-point_a[1])**2 + (point_b[0]-point_a[0])**2)
print('Distance between a and b: %.2f' % dist)