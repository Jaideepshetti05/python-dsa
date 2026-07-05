text = "java python java c python"

result = list(dict.fromkeys(text.split()))

print(result)