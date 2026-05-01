import atexit

def goodbye():
    print("App closing...")

atexit.register(goodbye)
print("Run program and exit")