data = {
    "apple":5,
    "banana":2,
    "orange":8,
    "grapes":4
}

sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_data)