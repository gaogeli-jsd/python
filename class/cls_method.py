# メソッド(method)
# クラスが持つ関数は メソッド と呼ばれます。
# メソッドもまた、どこからでも参照可能(public)です。
# メソッドの第一引数には、クラスのインスタンスを指定し、
# 第二引数以降で、メソッドの引数を受け取ります。

class MyClass:
    name = ""
    def setName(self, name):     # 第一引数は自インスタンス(self)
        self.name = name

a = MyClass()
a.setName("Tanaka")

print(a.name)