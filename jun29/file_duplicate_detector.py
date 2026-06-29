import hashlib
import os


def file_hash(filename):
    h = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


folder = input("Enter Folder Path: ")

hashes = {}

for filename in os.listdir(folder):

    path = os.path.join(folder, filename)

    if os.path.isfile(path):

        digest = file_hash(path)

        if digest in hashes:
            print("Duplicate:", filename, "<->", hashes[digest])
        else:
            hashes[digest] = filename