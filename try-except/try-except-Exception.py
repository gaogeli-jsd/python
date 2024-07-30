try:
    x = 10 / 2
    print(y)
except ZeroDivisionError:
    print("ゼロで除算することはできません。")
except FileNotFoundError:
    print("ファイルが見つかりませんでした。")
except Exception as e:
    print(f"予期しないエラーが発生しました: {e}")