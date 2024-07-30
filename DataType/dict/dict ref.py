# 全ての要素や値を参照するには、items(), keys(), valus(), items() を使用します。
# 参照される要素の順序は順不同です。

d = {'Yamada': 30, 'Suzuki': 40, 'Tanaka': 80}

for k, v in d.items():
    print(k, v)            # Tanaka 80, Yamada 30, Suzuki 40

for k in d.keys():
    print(k, d[k])         # Suzuki 40, Yamada 30, Tanaka 80

for v in d.values():
    print(v)               # 80, 30, 40

for k, v in d.items():
    print(k, v)            # Tanaka 80, Yamada 30, Suzuki 40