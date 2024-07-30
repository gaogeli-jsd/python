import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
#    '["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))

"""
#dict = {"name": "太郎", "age": 23, "gender": "男"}
#enc = json.dumps(dict, indent=2, ensure_ascii=False)
#print(enc)

dict = {"name": "tarou", "age": 23, "gender": "man"}

enc = json.dumps(dict)
s
print(dict)
print(type(dict))
print("******************")
print(enc)
print(type(enc))

"""