text = "programming"

seen = ""

for ch in text:
    if ch not in seen:
        seen += ch

print(seen)