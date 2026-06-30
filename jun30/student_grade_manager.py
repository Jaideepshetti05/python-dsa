n = int(input("Subjects: "))
marks = [int(input()) for _ in range(n)]
avg = sum(marks) / n

if avg >= 90:
    print("Grade A")
elif avg >= 75:
    print("Grade B")
elif avg >= 60:
    print("Grade C")
else:
    print("Fail")