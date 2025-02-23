
# It is possible to nest lists (create lists containing other lists), 
# for example:

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)            # -- [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])         # -- ['a', 'b', 'c']
print(x[0][1])      # -- 'b'