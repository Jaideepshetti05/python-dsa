import shutil

source = "sample.txt"
backup = "backup.txt"

shutil.copy(source, backup)
print("Backup Created")