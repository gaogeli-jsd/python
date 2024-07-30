import mysql.connector

# MySQLに接続
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="G@0MySQL"
)

# カーソルを取得
cursor = conn.cursor()

# use データベース
use_database = "USE mydatabase"
cursor.execute(use_database)

# 複数データ挿入のクエリ
insert_multiple_data_query = """
INSERT INTO users (username, email) VALUES (%s, %s), (%s, %s), (%s, %s)
"""

# 複数データ挿入
multiple_user_data = [
    ["Tanaka", "tanaka@example.com"],
    ["Yamada", "yamada@example.com"],
    ["Hashimoto", "hashimoto@example.com"]
]

cursor.executemany(insert_multiple_data_query, multiple_user_data)

# 変更を確定
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()