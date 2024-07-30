import os

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        print("root = " + root)
        for file in files:
            yield os.path.join(root, file)
            print("root = " + root)
#            print("dirs = " + dirs)
            print("file = " + file)
            
pathFrom = "C:\\kou\\study\\python\\test\\from"
for file in find_all_files(pathFrom):
    print (file)

