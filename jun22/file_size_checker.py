import os

file = "sample.txt"

if os.path.exists(file):
    print(os.path.getsize(file), "bytes")
else:
    print("File not found")