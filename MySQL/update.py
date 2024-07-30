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

# データ更新のクエリ
update_data_query = "UPDATE users SET email = %s WHERE username = %s"

# データ更新
new_email = "Tanaka.new@example.com"
cursor.execute(update_data_query, (new_email, "Tanaka"))

# 変更を確定
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()