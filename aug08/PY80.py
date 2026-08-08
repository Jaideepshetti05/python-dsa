s1 = "abcd"
s2 = "cdab"

if s2 in s1+s1:
    print("Rotation")
else:
    print("Not Rotation")