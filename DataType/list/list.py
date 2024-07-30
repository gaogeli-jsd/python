
# a list of comma-separated values (items) between square brackets. 
# Lists might contain items of different types, 
# but usually the items all have the same type.
squares = [1, 4, 9, 16, 25]
print(squares)      # -- [1, 4, 9, 16, 25]

# Like strings (and all other built-in sequence type), 
# lists can be indexed and sliced:
print(squares[0])  # indexing returns the item -- 1
print(squares[-1]) # -- 25
print(squares[-3:])  # slicing returns a new list -- [9, 16, 25]

# All slice operations return a new list containing the requested elements. 
# This means that the following slice returns a new (shallow) copy of the list:
print(squares[:])   # -- [1, 4, 9, 16, 25]

# Lists also support operations like concatenation:
squares2 = squares + [36, 49, 64, 81, 100]
print(squares2)  # -- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]