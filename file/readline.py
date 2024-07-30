
path = "C:\\kou\\study\\python\\file\\abc.txt"

output_rows = []
with open(path) as f:
    for s_line in f:
        print(repr(s_line))
        if "999999" not in s_line:
            output_rows.append(s_line)
print(output_rows)        
# 'line 1\n'
# 'line 2\n'
# 'line 3'