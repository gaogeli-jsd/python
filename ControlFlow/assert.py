# アサーション文(assert)
# assert はテストの際に値が期待通りに設定されているかを確認するための仕組みです。
# __debug__ が True の時のみ動作し、式を評価して偽であれば、
# AssertionError例外を発生させます。
# python を -O オプション付きで起動することで、
# __debug__ の値は False になります。

def func():
    return 5

f = func()
assert f == 5              # f の値が期待通り 5になっていることを確認する

'''
assert expression は、下記と等価です。
if __debug__:
    if not expression: raise AssertionError

assert expression1, expression2 は、下記と等価です。
if __debug__:
    if not expression1: raise AssertionError(expression2)
'''