
# A special problem is the construction of tuples containing 0 or 1 items: 
# the syntax has some extra quirks to accommodate these. 
# Empty tuples are constructed by an empty pair of parentheses;
# a tuple with one item is constructed by following a value with a comma
#  (it is not sufficient to enclose a single value in parentheses).
#  Ugly, but effective. For example:

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))       # -- 0
print(len(singleton))   # -- 1
print(singleton)        # -- ('hello',)
