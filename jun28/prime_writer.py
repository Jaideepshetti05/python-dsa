with open("prime.txt","w") as f:
    for i in range(2,101):
        if all(i%j for j in range(2,int(i**0.5)+1)):
            f.write(f"{i}\n")