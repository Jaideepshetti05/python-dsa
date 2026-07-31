text="Artificial Intelligence".lower()

vowels="aeiou"

v=c=0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v+=1
        else:
            c+=1

print(v,c)