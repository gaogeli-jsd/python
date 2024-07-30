# ロギングのカスタマイズ
# basicConfig() を用いてコンフィグの
#       出力先ファイル名、
#       レベル、
#       フォーマット
# 等を変更することができます。
import logging
logging.basicConfig(
    filename="example.log",
    level=logging.DEBUG,
    format="[%(levelname)s] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p"
)

logging.debug("This is DEBUG message.")
logging.info("This is INFO message.")
logging.warning("This is WARNING message.")
logging.error("This is ERROR message.")
logging.critical("This is CRITICAL message.")