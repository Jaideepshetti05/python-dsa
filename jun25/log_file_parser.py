from collections import Counter

filename = "server.log"

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    levels = []

    for line in lines:
        if "INFO" in line:
            levels.append("INFO")
        elif "WARNING" in line:
            levels.append("WARNING")
        elif "ERROR" in line:
            levels.append("ERROR")

    count = Counter(levels)

    print("Log Summary")
    print("-" * 25)

    for level, total in count.items():
        print(f"{level}: {total}")

except FileNotFoundError:
    print("server.log file not found.")