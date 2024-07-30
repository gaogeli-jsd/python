import os

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

# read from file
def readFile(inFile):
    return_rows = []
#   for line in open(filename, 'r', encoding="utf-8"):
    with open(inFile, 'r', encoding="utf-8") as f:
        for s_line in f:
            print(repr(s_line))
            # 特定の行を排除
            if "◆◆◆" not in s_line:
                return_rows.append(s_line)
    return return_rows

# write to file
def writeFile(outFile, content):
    with open(outFile, 'w', encoding="utf-8") as f:
        print(content)
        f.writelines(content)

output_rows = []



pathFrom = "C:\\kou\\study\\python\\test\\from"
pathTo = "C:\\kou\\study\\python\\test\\to"
for file in find_all_files(pathFrom):
    print (file)
    fileTo = file.replace(pathFrom, pathTo)
    print (fileTo)
    if os.path.isdir(file):
        print(f'* {file} is a directory.')
        if os.path.isdir(fileTo):
            print(f'** {fileTo} is a directory.')
        else:
            print(f'** {fileTo} directory ---> make.') 
            os.mkdir(fileTo)
    else:
        print("◆ make file !") 
        output_rows = readFile(file)     
        print(output_rows)
        writeFile(fileTo,output_rows)       