# グローバル変数(global)
# 関数の外部で定義された変数は グローバル変数 として扱われます。
# 関数の中でグローバル変数を参照することはできますが、代入することはできません。
# 代入する場合は、global で宣言する必要があります。

count = 0                   # グローバル変数

def func1():
    print(count)            # 参照することはできる

def func2():
    global count            # global宣言してやれば
    count += 1              # 代入することもできる

#globals() はグローバル変数、locals() はローカル変数の一覧を辞書として返却します。

def func():
    for k in globals().keys():
        print("GLOBAL: %s = %s" % (k, globals()[k]))
    for k in locals().keys():
        print("LOCAL: %s = %s" % (k, locals()[k]))

func()