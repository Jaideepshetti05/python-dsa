hour = 5
minute = 45

angle = abs((30 * hour + 0.5 * minute) - (6 * minute))
print(min(angle, 360 - angle))