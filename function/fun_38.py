# Python 3.8 以降では引数に / を指定すると
#  / より前の引数は位置専用引数とみなすようになりました。
# 位置専用引数はキーワードを指定することができません。

def func(a, b, /, c):
   print("a=%s, b=%s, c=%s" % (a, b, c))

func("A", "B", "C")             # a=A, b=B, c=C
func("A", "B", c="C")           # a=A, b=B, c=C
# func(a="A", b="B", c="C")       # aやbにキーワードを指定したのでTypeError