from multiprocessing import Process

def worker():
    print("Child Process")

p = Process(target=worker)
p.start()
p.join()