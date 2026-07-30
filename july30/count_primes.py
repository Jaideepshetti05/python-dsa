count = 0

for n in range(2,101):
    prime = True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
    if prime:
        count+=1

print(count)