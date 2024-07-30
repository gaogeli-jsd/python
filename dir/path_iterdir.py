import os
from pathlib import Path

pathFrom = "C:\\kou\\study\\python\\test\\from"

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

for file in find_all_files('/tmp/test'):
    print file



# Pathオブジェクトを生成
p = Path(pathFrom)

# dir_A直下のファイルとディレクトリを取得
# Path.glob(pattern)はジェネレータを返す。結果を明示するためlist化しているが、普段は不要。
list(p.glob("*"))

# ファイル名の条件指定
list(p.glob("*.txt"))

# 再帰的な検索
list(p.glob("**/*"))

#is_dir = os.path.isdir(pathFrom)
#print(pathFrom)
#print(is_dir)  # True または False

