import os

# os.getcwd()でカレントディレクトリの絶対パスができている。
print('getcwd:      ', os.getcwd())

# __file__でpython3コマンドで指定したパスが取得できている。
print('__file__:    ', __file__)

# 実行中のファイルのファイル名
print('basename:    ', os.path.basename(__file__))

# 実行中のファイルのディレクトリ名
print('dirname:     ', os.path.dirname(__file__))

# __file__で相対パスを取得した場合はos.path.abspath()で絶対パスに変換できる。
print('abspath:     ', os.path.abspath(__file__))

# __file__で相対パスを取得した場合はos.path.abspath()で絶対パスに変換できる。ディレクトリも絶対パスで取得可能。
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))