# リストの内包表記
# リストの内包表記 を用いることで、
# map(), filter(), lambda を使用しないで
# 簡単なリスト演算を行うことができます。

a = [1, 2, 3]
print([x * 2 for x in a])                       #=> [2, 4, 6]
print([x * 2 for x in a if x == 3])             #=> [6]
print([[x, x * 2] for x in a])                  #=> [[1, 2], [2, 4], [3, 6]]
print([(x, x * 2) for x in a])                  #=> [(1, 2), (2, 4), (3, 6)]

b = [4, 5, 6]
print([x * y for x in a for y in b])            #=> [4, 5, 6, 8, 10, 12, 12, 15, 18]
print([a[i] * b[i] for i in range(len(a))])     #=> [4, 10, 18]