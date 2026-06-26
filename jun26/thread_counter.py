import threading
import time

def counter(name):
    for i in range(1, 11):
        print(f"{name}: {i}")
        time.sleep(0.5)

t1 = threading.Thread(target=counter, args=("Thread-1",))
t2 = threading.Thread(target=counter, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads finished.")