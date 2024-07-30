
# The statement t = 12345, 54321, 'hello!' is an example of tuple packing: 
# the values 12345, 54321 and 'hello!' are packed together in a tuple. 
# The reverse operation is also possible:

t = 12345, 54321, 'hello!'
x, y, z = t
print(t)    # -- (12345, 54321, 'hello!')
print(x)    # -- 12345
print(y)    # -- 54321
print(z)    # -- hello!