# ビルトインモジュール(__builtin__)
# __builtin__ は、open() などのビルトインオブジェクト
# を包含する仮想的なモジュールを示します。

# ????????????????????  要調査

import __builtin__

for line in __builtin__.open("test.txt"):
    print(line)