import os

folder = input("Enter Folder Path: ")

files = os.listdir(folder)

count = 1

for file in files:

    if file.lower().endswith(".pdf"):

        old_path = os.path.join(folder, file)

        new_name = f"Document_{count}.pdf"

        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)

        print(file, "->", new_name)

        count += 1

print("Renaming Completed.")