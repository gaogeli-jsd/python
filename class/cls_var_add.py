# クラス変数やインスタンス変数は、動的に追加することができます。

class MyClass:
    pass

a1 = MyClass()
a1.name2 = "Tanaka"                 # インスタンス変数の追加
MyClass.PI2 = 3.141593              # クラス変数の追加