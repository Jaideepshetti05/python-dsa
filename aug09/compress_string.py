    def compress(text):
    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(text[i - 1] + str(count))
            count = 1

    if text:
        result.append(text[-1] + str(count))

    return "".join(result)


print(compress("aaabbccccdaa"))