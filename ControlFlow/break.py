# ループを抜ける(break)
# break は最も内側の while, for などのループ処理を抜けます。
# 下記の例では n が 5の時に forループを抜けます。

for n in range(10):
    if n == 5:
        break
    print(n)                 # 0, 1, 2, 3, 4