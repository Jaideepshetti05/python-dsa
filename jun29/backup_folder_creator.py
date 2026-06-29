import shutil
import os
from datetime import datetime

source = input("Enter Source Folder: ")
destination = input("Enter Backup Location: ")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_folder = os.path.join(destination, f"Backup_{timestamp}")

shutil.copytree(source, backup_folder)

print("\nBackup Created Successfully!")
print("Location:", backup_folder)