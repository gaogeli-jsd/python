'''
～のあいだ(for, in)
文法
for var in expr:
    suite1...
[else:
    suite2...]
for はリスト、タプルの各要素、辞書のキー、文字列の各文字、ファイルの各行などに対して処理 suite1 を繰り返します。
'''

for n in [1, 2, 3]:          # 配列
    print(n)                 #=> 1, 2, 3

for n in (1, 2, 3):          # タプル
    print(n)                 #=> 1, 2, 3

for c in "ABC":              # 文字列
    print(c)                 #=> A, B, C

for k in {'one': 1, 'two': 2, 'three': 3}:   # 辞書
    print(k)                                 #=> one, two, three

for line in open("test.txt"):              # ファイルの中身
    print(line)                              # 1行ずつ表示