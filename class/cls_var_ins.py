# クラス変数・インスタンス変数(attribute)
# クラスは、インスタンス変数 と クラス変数 を持つことができます。
# インスタンス変数は「インスタンス.変数名」で表され、インスタンス毎に独立の変数です。
# コンストラクタ __init__(後述)の中で初期化することをお勧めします。

class MyClass:
    def __init__(self):
        self.name = ""              # インスタンス変数

a1 = MyClass()
a1.name = "Tanaka"

a2 = MyClass()
a2.name = "Suzuki"

print(a1.name)                       #=> Tanaka
print(a2.name)                       #=> Suzuki