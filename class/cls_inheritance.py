# 継承(inheritance)
# 他のオブジェクト指向言語と同様、クラスを継承することもできます。
# 下記の例では、MyClassクラスを継承した、
# MyClass2サブクラスを定義しています。
# サブクラスでは、親クラスが持つアトリビュートやメソッドを
# 継承して利用することができます。

class MyClass:
    def hello(self):
        print("Hello")

class MyClass2(MyClass):
    def world(self):
        print("World")

a = MyClass2()
a.hello()                   #=> Hello
a.world()                   #=> World