import psutil
import time

while True:
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    time.sleep(2)