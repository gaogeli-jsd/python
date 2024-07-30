# インポート(import)
# パッケージの中からモジュールや識別子(クラス、関数、変数...)
# をインポートするには下記の様にします。

# import [パッケージ.]モジュール
import mypack1.mypack2.mymod
print(" ---------- 07 --------- ")
mypack1.mypack2.mymod.myfunc()

# from パッケージ import モジュール
from mypack1.mypack2 import mymod
print(" ---------- 11 --------- ")
mymod.myfunc()

# from パッケージ import *
from mypack1.mypack2 import *                # __all__の設定が必要
print(" ---------- 17 --------- ")
mymod.myfunc()

# from [パッケージ.]モジュール import 識別子
from mypack1.mypack2.mymod import myfunc
print(" ---------- 22 --------- ")
myfunc()

# from [パッケージ.]モジュール import *
from mypack1.mypack2.mymod import *
print(" ---------- 27 --------- ")
myfunc()