def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(
                    dp[value],
                    dp[value - coin] + 1
                )

    return -1 if dp[amount] == float("inf") else dp[amount]


coins = [1, 2, 5]
amount = 11

print("Minimum coins:", coin_change(coins, amount))