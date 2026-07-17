def check(s):
    stack=[]
    pair={')':'(',']':'[','}':'{'}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack.pop()!=pair[ch]:
                return False
    return not stack

print(check("{[()]}"))