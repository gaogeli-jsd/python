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

# テーブル作成のクエリ
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
)
"""

# テーブル作成
cursor.execute(create_table_query)

# 接続を閉じる
cursor.close()
conn.close()