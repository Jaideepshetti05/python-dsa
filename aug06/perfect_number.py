num = 28

s = sum(i for i in range(1,num) if num%i==0)

print(s == num)