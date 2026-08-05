data={"a":5,"b":2,"c":8,"d":1}

sorted_data=dict(sorted(data.items(), key=lambda x:x[1]))

print(sorted_data)