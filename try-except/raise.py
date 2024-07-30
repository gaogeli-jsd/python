def check_value(value):
    if value < 0:
        raise ValueError("負の値は許可されていません。")
    return value

try:
    result = check_value(5-1)
    strResult = str(result)
    print(" strResult = " + strResult)
except ValueError as e:
    print(e)