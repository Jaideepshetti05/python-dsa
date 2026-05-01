text = "hello"
enc = ''.join(chr(ord(c)+2) for c in text)
print(enc)