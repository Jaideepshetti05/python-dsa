import json

with open("file1.json") as f1, open("file2.json") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

merged = {**data1, **data2}

with open("merged.json", "w") as f:
    json.dump(merged, f, indent=4)

print("Merged successfully")