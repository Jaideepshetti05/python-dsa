stack = []

pairs = {')':'(', ']':'[', '}':'{'}

text = "{[()]}"

ok = True

for ch in text:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack.pop() != pairs[ch]:
            ok = False
            break

print(ok and not stack)