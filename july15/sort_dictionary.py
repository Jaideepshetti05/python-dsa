students = {
    "John":80,
    "Alex":92,
    "Sam":75
}

for k,v in sorted(students.items(), key=lambda x:x[1]):
    print(k,v)