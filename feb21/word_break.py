def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for word in wordDict:
            if i >= len(word) and s[i-len(word):i] == word:
                dp[i] = dp[i] or dp[i-len(word)]

    return dp[len(s)]