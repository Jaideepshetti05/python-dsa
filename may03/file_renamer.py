import os

folder = input("Folder path: ")

for i, file in enumerate(os.listdir(folder)):
    os.rename(f"{folder}/{file}", f"{folder}/file_{i}.txt")

print("Renamed successfully")