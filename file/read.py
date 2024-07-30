# ファイルパス
file_path = "data.csv"

# ファイルオープン
f = open(file_path, "r", encoding="utf-8")

# 読み込み
s = f.read()

print(s)

# ファイルクローズ
f.close()