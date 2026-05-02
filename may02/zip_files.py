import zipfile

with zipfile.ZipFile('files.zip', 'w') as z:
    z.write('file1.txt')