# CSV形式でデータを保存
with open('data.csv', 'w') as f:
    rows = ['name,age\n', 'Alice,30\n', 'Bob,40\n']
    rows.append("one\n")
    rows.append("two\n")
    print(rows)
    f.writelines(rows)