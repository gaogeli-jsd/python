# マッチ文(match)
#Python 3.10 で追加された機能で、他言語の switch case に相当します。
# マッチしなかった場合は case _ が実行されます。

# Python 3.10～
c = 3
match c:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")