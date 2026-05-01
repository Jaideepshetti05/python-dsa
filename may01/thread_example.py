import threading

def task():
    print("Thread running")

t = threading.Thread(target=task)
t.start()