# 関数の戻り値としてタプルを返却することもできます。

def get_date():
    return 2022, 10, 9

year, month, day = get_date()
print("%04d/%02d/%02d" % (year, month, day))   # 2022/10/09