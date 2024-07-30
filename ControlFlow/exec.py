# exec文(exec)
# exec文(exec)は、引数の文字列を Python のスクリプトとして実行します。

#文法
#exec(statements [, global [, local]])
#サンプルを下記に示します。
exec("print('Hello')")

#global と local には、グローバル変数、ローカル変数を辞書形式で渡します。
# ローカル変数を省略した場合は、global が両方に適用されます。
exec("print(global_x, local_y)", {'global_x': 100}, {'local_y': 200})