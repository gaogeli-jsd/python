# 多重継承
# Python では多重継承がサポートされています。
# 下記では、MyClassA, MyClassB 両方を継承する MyClassC を定義しています。

class MyClassA:
    def funcA(self):
        print("MyClassA:funcA")

class MyClassB:
    def funcB(self):
        print("MyClassB:funcB")

class MyClassC(MyClassA, MyClassB):
    pass

a = MyClassC()
a.funcA()                    # MyClassA のメソッドも
a.funcB()                    # MyClassB のメソッドも使用できる