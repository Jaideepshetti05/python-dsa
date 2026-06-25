temperatures = []

days = int(input("Enter number of days: "))

for i in range(days):
    temp = float(input(f"Temperature Day {i+1}: "))
    temperatures.append(temp)

print("\nAverage Temperature:", sum(temperatures) / len(temperatures))
print("Maximum Temperature:", max(temperatures))
print("Minimum Temperature:", min(temperatures))