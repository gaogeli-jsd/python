# map() はリストの各要素に対して処理を行い、行った結果を返します。
# 下記の例では各要素を2倍にする処理を行います。

a = [1, 2, 3]

def double(x): return x * 2

print(list(map(double, a)))                  #=> [2, 4, 6] : 関数方式
print(list(map(lambda x: x * 2, a)))         #=> [2, 4, 6] : lambda方式
print([x * 2 for x in a])                    #=> [2, 4, 6] : 内包表記(後述)