
fileFrom = "C:\\kou\\study\\python\\file\\fileFrom.txt"
fileTo = "C:\\kou\\study\\python\\file\\fileTo.txt"

# read from file
def readFile(inFile):
    return_rows = []
    with open(inFile) as f:
        for s_line in f:
            print(repr(s_line))
            # 特定の行を排除
            if "999999" not in s_line:
                return_rows.append(s_line)
    return return_rows

# write to file
def writeFile(outFile, content):
    with open(outFile, 'w') as f:
        print(content)
        f.writelines(content)

output_rows = []
output_rows = readFile(fileFrom)     

print(output_rows)
writeFile(fileTo,output_rows)
