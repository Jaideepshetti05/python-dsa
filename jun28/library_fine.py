days=int(input())

if days<=7:
    fine=days*2
else:
    fine=(7*2)+(days-7)*5

print("Fine =",fine)