num = 29

count = 0

while num:
    count += num & 1
    num >>= 1

print("Set Bits:", count)