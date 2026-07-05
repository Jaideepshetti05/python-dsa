balance = 5000

while True:
    print("1 Deposit")
    print("2 Withdraw")
    print("3 Balance")
    print("4 Exit")

    ch = int(input())

    if ch == 1:
        balance += float(input())

    elif ch == 2:
        balance -= float(input())

    elif ch == 3:
        print(balance)

    else:
        break