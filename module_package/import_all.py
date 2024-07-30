# 「from パッケージ import *」の形式を用いるには、
# mypack2 パッケージの __init__.py ファイル
# に読み込み対象のモジュールリスト
# を __all__ に定義しておく必要があります。


# from パッケージ import *
from mypack1.mypack2 import *                # __all__の設定が必要
mymod.myfunc()
