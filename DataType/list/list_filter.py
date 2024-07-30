# filter() はリストの各要素に対して処理を行い、
# 処理結果が真となる要素のみを取り出します。
# 下記の例では各要素から奇数のみを取り出します。

a = [1, 2, 3]

def isodd(x): return x % 2
print(list(filter(isodd, a)))              #=> [1, 3] : 関数方式
print(list(filter(lambda x: x % 2, a)))    #=> [1, 3] : lambda方式
print([x for x in a if x % 2])             #=> [1, 3] : 内包表記(後述)