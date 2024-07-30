# モジュール(module)
# ひとつのスクリプトファイルはモジュールとして扱うことができます。
# モジュールは import文で読み込みます。
# 読み込んだモジュールのクラス、関数、変数は、
# 「モジュール名.識別子」で参照することができます。

# mymod.py
def myfunc():
    print("Hello!")
# mytest.py
import mymod

mymod.myfunc()                      #=> Hello!
# モジュールの冒頭には、"""...""" で ドキュメントストリング を記述することができます。


# coding: utf-8
"""A sample module"""
