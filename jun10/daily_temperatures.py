temps = [73,74,75,71,69,72,76,73]

stack = []
result = [0] * len(temps)

for i, temp in enumerate(temps):
    while stack and temp > temps[stack[-1]]:
        idx = stack.pop()
        result[idx] = i - idx

    stack.append(i)

print(result)