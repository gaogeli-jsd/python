# デストラクタ(__del__)
# __del__() メソッドは、クラスのインスタンスが消滅する際に呼び出されます。
# デストラクタ とも呼ばれます。
class MyClass:
    def __init__(self):
        print("INIT!")
    def __del__(self):
        print("DEL!")

a = MyClass()           #=> INIT!
del a                   #=> DEL!