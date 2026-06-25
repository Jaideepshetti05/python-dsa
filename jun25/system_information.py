import platform
import os

print("System Information")
print("-" * 30)

print("Operating System :", platform.system())
print("Release          :", platform.release())
print("Version          :", platform.version())
print("Machine          :", platform.machine())
print("Processor        :", platform.processor())
print("Current Directory:", os.getcwd())