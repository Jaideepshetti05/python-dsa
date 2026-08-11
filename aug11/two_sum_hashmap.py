arr = [4, 7, 1, 9, 3]
target = 10

seen = {}

for i, num in enumerate(arr):
    required = target - num

    if required in seen:
        print("Pair:", required, "+", num)
        break

    seen[num] = i
else:
    print("No pair found")