for n in range(100,1000):
    if n == sum(int(d)**3 for d in str(n)):
        print(n)