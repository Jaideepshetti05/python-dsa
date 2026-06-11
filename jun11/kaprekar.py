num = int(input("Enter number: "))

sq = str(num * num)
mid = len(sq) // 2

left = int(sq[:mid] or 0)
right = int(sq[mid:] or 0)

if left + right == num:
    print("Kaprekar Number")
else:
    print("Not Kaprekar Number")