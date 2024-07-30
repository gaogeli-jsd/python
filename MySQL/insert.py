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

# データ挿入のクエリ
insert_data_query = """
INSERT INTO users (username, email) VALUES (%s, %s)
"""

# データ挿入
user_data = ("Tanaka", "tanaka@example.com")
cursor.execute(insert_data_query, user_data)

# 変更を確定
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()