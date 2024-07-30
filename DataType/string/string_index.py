word = 'Python'

# Strings can be indexed (subscripted), 
# with the first character having index 0. 
# There is no separate character type;
# a character is simply a string of size one:
print(word[0])  # character in position 0 -- P
print(word[5])  # character in position 5 -- n

# Indices may also be negative numbers, to start counting from the right:
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])

"""  出力結果：
P
n
n
o
P
"""