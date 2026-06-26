def calculate_statistics(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)


marks = [85, 92, 78, 66, 95, 88]

calculate_statistics(marks)