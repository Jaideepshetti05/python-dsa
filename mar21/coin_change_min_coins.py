def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for curr_amount in range(coin, amount + 1):
            dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = 5
print(f"Min coins for {amount}: {coinChange(coins, amount)}")
