# File: list_intersection.py
def intersection(a, b):
    return list(set(a) & set(b))

print(intersection([1,2,3], [2,3,4]))