text = "HELLO"
shift = 3

cipher = ""

for ch in text:
    cipher += chr((ord(ch)-65+shift)%26+65)

print(cipher)