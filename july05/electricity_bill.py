u = int(input("Units: "))

if u <= 100:
    bill = u * 2
elif u <= 300:
    bill = 200 + (u - 100) * 3.5
else:
    bill = 900 + (u - 300) * 5

print("Bill =", bill)