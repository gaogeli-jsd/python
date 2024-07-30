
# In addition to indexing, slicing is also supported. 
# While indexing is used to obtain individual characters, 
# slicing allows you to obtain substring:
word = 'Python'
print(word[0:2])  # characters from position 0 (included) to 2 (excluded) -- 'Py'
print(word[2:5])  # characters from position 2 (included) to 5 (excluded) -- 'tho'

# Note how the start is always included, 
# and the end always excluded. 
# This makes sure that s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])      # 'Python'
print(word[:4] + word[4:])      # 'Python'