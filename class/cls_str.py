# __str__() は、インスタンスを暗黙的に文字列に変換する際の変換処理を定義します。
class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name

a = MyClass("Yamada")
print(a)                       #=> My name is Yamada