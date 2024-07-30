# reduce() はリストの最初の2要素を引数に処理を呼び出し、
# 結果と次の要素を引数に処理の呼び出しを繰り返し、単一の結果を返します。
# 下記の例では、各要素の合計を計算しています。

from functools import reduce

a = [1, 2, 3, 4, 5]

def add(x, y): return x + y
print(reduce(add, a))                  #=> 15 : 関数方式
print(reduce(lambda x, y: x + y, a))   #=> 15 : lambda方式