# 辞書(dict)
# {...} は、辞書(dict)と呼ばれるキーと値のペアのリストを保持します。
d = {'Yamada': 30, 'Suzuki': 40, 'Tanaka': 80}

# 各要素には次のようにアクセスします。
d1 = d['Yamada']
d2 = d['Suzuki']
d3 = d['Tanaka']

# 要素を追加するには次のようにします。
d['Kimura'] = 60

# 全ての要素や値を参照するには、items(), ・・・を使用します。
# 参照される要素の順序は順不同です。
for k, v in d.items():
    print(k, v)

