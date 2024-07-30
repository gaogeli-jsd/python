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

# データ削除のクエリ
delete_data_query = "DELETE FROM users WHERE username = %s"

# データ削除
cursor.execute(delete_data_query, ("Tanaka"))

# 変更を確定
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()