# イテレータ(iterator)
# イテレータ は for などで使用することができる繰り返し機能を持つオブジェクトです。
# イテレータオブジェクトは、
# __iter__() で __next__() メソッドを持つオブジェクトを返却し、
# __next__() メソッドは次の要素を返却し、
# 最後に達すると StopIteration 例外を返すことで実装できます。

class MyRange:
    def __init__(self, max):
        self._max = max
        print(" hi from -- init !")

    def __iter__(self):
        self._count = 0
        print(" hi from -- iter !")
        return self

    def __next__(self):
        result = self._count
        if result >= self._max:
            raise StopIteration
        self._count += 1
        print(" hi from -- next !")
        print(" hi from -- result = %s !" % result)
        return result

for n in MyRange(6):
    print(n)                    #=> 0, 1, 2, 3, 4