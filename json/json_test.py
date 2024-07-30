import json

data = {
    "name": "山田太郎",
    "age": 36
}

data_str = json.dumps(data, indent=4, ensure_ascii=False)
data_obj = json.loads(data_str)

print(data_str)
print(data_obj)