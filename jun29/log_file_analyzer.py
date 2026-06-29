filename = "server.log"

errors = 0
warnings = 0
info = 0

with open(filename, "r") as file:

    for line in file:

        line = line.upper()

        if "ERROR" in line:
            errors += 1
        elif "WARNING" in line:
            warnings += 1
        elif "INFO" in line:
            info += 1

print("Log Analysis")
print("-" * 25)
print("Errors   :", errors)
print("Warnings :", warnings)
print("Info     :", info)