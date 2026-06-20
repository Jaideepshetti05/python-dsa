text = "java python java c python"
result = " ".join(dict.fromkeys(text.split()))
print(result)