import json

data = {"name":"Alice","age":22}

with open("data.json","w") as f:
    json.dump(data,f)

with open("data.json") as f:
    print(json.load(f))