nested = [[1,2],[3,4],[5,6]]

flat = [item for sub in nested for item in sub]

print(flat)