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

# データ取得のクエリ
select_one_data_query = "SELECT * FROM users WHERE username = 'Tanaka'"

# データ取得
cursor.execute(select_one_data_query)

# 結果を取得
result = cursor.fetchone()

# 結果を表示
print(result)

# 接続を閉じる
cursor.close()
conn.close()