try:
    x = 10 / 2
except ZeroDivisionError:
    print("ゼロで除算することはできません。")
finally:
    print("処理が完了しました。")