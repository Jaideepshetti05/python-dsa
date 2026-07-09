values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

roman = "MCMXCIV"

total = 0

for i in range(len(roman)):
    if i+1 < len(roman) and values[roman[i]] < values[roman[i+1]]:
        total -= values[roman[i]]
    else:
        total += values[roman[i]]

print(total)