# ノンローカル変数(nonlocal)
# nonlocal は、変数がグローバル変数でもローカル変数でもない変数ないことを示します。
# 下記の例で、count 変数はグローバル変数
#  count でもなく、count_up() 関数のローカル変数でもなく、
# counter() 関数のローカル変数を参照します。

count = 999               # グローバル変数

def counter():
    count = 0             # count_up()から見るとローカルではない変数
    def count_up():
        nonlocal count    # グローバルでもローカルでもない親関数の変数を参照
        count += 1
        return count
    return count_up

cnt = counter()
print(cnt())              #=> 1
print(cnt())              #=> 2
print(cnt())              #=> 3