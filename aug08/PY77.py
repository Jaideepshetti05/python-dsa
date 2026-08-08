n = 28

s = sum(i for i in range(1,n) if n%i==0)

print("Perfect" if s==n else "Not Perfect")