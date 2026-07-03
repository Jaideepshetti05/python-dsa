import threading

def task():
    print("Thread Running")

t = threading.Thread(target=task)
t.start()
t.join()