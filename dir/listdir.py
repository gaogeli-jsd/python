import os

dir_path = "c:\\kou\\study\\python\\test"

files = os.listdir(dir_path)
print(files)
# ['file2.txt', 'dir2', 'file3.jpg', 'file1', 'dir1']

print(type(files))
# <class 'list'>