# インデントにタブ文字(U+0009)を用いる場合、
# 半角スペースを用いるか、
# タブ文字を用いるか統一が必要です。
# 統一されていない場合 TabError: 
# inconsistent use of tabs and spaces in indentation
#  エラーが発生します。

a=5
if a == 5:
    print("AAA")      # この行は半角スペースインデントなのに
#[=TAB==]print("BBB")      # この行がタブインデントだと TabError
