import os

old = "old.txt"
new = "new.txt"

if os.path.exists(old):
    os.rename(old, new)