# 親クラス(super())
# super() は 親クラス を参照します。
# 第一引数にはクラス、第二引数にはインスタンスを指定します。
# 下記の例では、サブクラスのコンストラクタの中で、
# 親クラスのコンストラクタを呼び出しています。

class MyClass1(object):
    def __init__(self):
       self.val1 = 123

class MyClass2(MyClass1):
    def __init__(self):
#        super(MyClass2, self).__init__()
        self.val2 = 456

a = MyClass2()
print(a.val1)               #=> 123
print(a.val2)               #=> 456