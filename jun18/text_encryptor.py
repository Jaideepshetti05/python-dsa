text = input("Enter text: ")

encrypted = ''.join(
    chr(ord(c)+2)
    for c in text
)

print(encrypted)