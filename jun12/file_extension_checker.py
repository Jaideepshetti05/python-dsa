filename = input("Enter file name: ")

if "." in filename:
    extension = filename.split(".")[-1]
    print("Extension:", extension)
else:
    print("No extension found")