with open("server.log") as f:
    lines = f.readlines()

errors = [line for line in lines if "ERROR" in line]
print("Error count:", len(errors))