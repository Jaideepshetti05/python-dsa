import os

path = "."

total_size = 0

for root, dirs, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)

        if os.path.isfile(file_path):
            total_size += os.path.getsize(file_path)

print(f"Total Size: {total_size} bytes")