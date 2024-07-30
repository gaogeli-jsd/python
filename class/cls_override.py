# サブクラスでは、親クラスのメソッドを上書き(オーバーライド)することができます。

class MyClass:
    def hello(self):
        print("Hello")

class MyClass2(MyClass):
    def hello(self):        # 親クラスのhello()メソッドをオーバーライド
        print("HELLO")

a = MyClass2()
a.hello()                   #=> HELLO