# ループを繰り返す(continue)
# continue は最も内側の while, for などのループ処理を繰り返します。
# 下記の例では n が 5の時に forループの先頭に戻ります。

for n in range(10):
    if n == 5:
        continue
    print(n)                 # 0, 1, 2, 3, 4, 6, 7, 8, 9