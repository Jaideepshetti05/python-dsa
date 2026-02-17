def is_valid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

print(is_valid("({[]})"))
