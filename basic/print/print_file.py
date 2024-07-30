# Python 3 で標準出力以外に出力するには、
#  file= を用います。

f = open("test.txt", "w")
print("Hello world!", file=f)
f.close()