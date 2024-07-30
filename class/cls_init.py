# コンストラクタ(__init__)
# __init__() メソッドは、クラスのインスタンスが生成された際に呼び出されます。
# コンストラクタ とも呼ばれます。

class MyClass:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

a = MyClass("Tanaka")
print(a.getName())                     #=> Tanaka