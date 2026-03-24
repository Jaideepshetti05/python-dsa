# File: frequency_count.py
from collections import Counter

def count_freq(lst):
    return Counter(lst)

print(count_freq([1,2,2,3,3,3]))