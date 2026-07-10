num = 1994

values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

ans = ""

for v,s in zip(values,symbols):
    while num >= v:
        ans += s
        num -= v

print(ans)