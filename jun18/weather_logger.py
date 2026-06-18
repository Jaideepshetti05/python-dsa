temp = 28

with open("weather.log","a") as f:
    f.write(f"Temperature: {temp}\n")

print("Logged")