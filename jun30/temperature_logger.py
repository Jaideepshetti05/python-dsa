with open("temperature.txt", "w") as f:
    for i in range(20, 31):
        f.write(str(i) + "\n")

print("Saved")