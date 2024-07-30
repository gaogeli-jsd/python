# 基本的なロギング
# ロギングによる出力
# 下記の様にしてログを出力します。

import logging

logging.debug("This is DEBUG message.")
logging.info("This is INFO message.")
logging.warning("This is WARNING message.")
logging.error("This is ERROR message.")
logging.critical("This is CRITICAL message.")

# 下記の様にフォーマットを指定することもできます。
filename = "logFile.log"
logging.error("Can't open file: %s", filename)

# ログレベルをメソッド名ではなく第一引数で指定することもできます。
logging.log(logging.ERROR, "...")

# 文字列からログレベルを得るには getattr() を使用します。
level = getattr(logging, "ERROR")
logging.log(level, "...")