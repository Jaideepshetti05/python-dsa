import os
import shutil

for file in os.listdir():
    if file.endswith(".txt"):
        shutil.move(file, "text_files/" + file)