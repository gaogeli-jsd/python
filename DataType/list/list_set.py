# セット(set)
# セット(set)は、重複の無いリストを扱います。
# セット同士の減算、OR、AND、XOR 操作が可能です。

a = set(['red', 'blue', 'green'])
b = set(['green', 'yellow', 'white'])

print(a)               #=> set(['red', 'blue', 'green'])
print(b)               #=> set(['green', 'yellow', 'white'])
print(a - b)           #=> set(['red', 'blue'])
print(a | b)           #=> set(['red', 'blue', 'green', 'yellow', 'white'])
print(a & b)           #=> set(['green'])
print(a ^ b)           #=> set(['red', 'blue', 'yellow', 'white'])
print('green' in a)    #=> True
a.add('black')
print(a)               #=> set(['red', 'blue', 'green', 'black'])