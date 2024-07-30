# アクセス制限(_, __)
# Python では private や protected などのアクセス修飾子はサポートされていません。
# アンダーバー(_)で始まる変数や関数は外から参照しないという慣習的ルールがあります。
# アンダーバー2個(__)で始まる変数や関数は参照が制限されます。

class MyClass:
    def __init__(self):
        self.name = "tanaka"
        self._name = "yamada"
        self.__name = "suzuki"

    def hello(self): print('hello')
    def _hello(self): print('hello')
    def __hello(self): print('hello')

a = MyClass()

print(a.name)           # 参照できる
print(a._name)          # 参照できるが慣習的に参照しない
# print(a.__name)       # 参照できない(AttributeError例外)

a.hello()               # 参照できる
a._hello()              # 参照できるが慣習的に参照しない
# a.__hello()           # 参照できない(AttributeError例外)