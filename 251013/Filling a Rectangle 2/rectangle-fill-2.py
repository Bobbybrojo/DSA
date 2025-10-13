n = int(input())


# dp[i] represents the number of ways to fill a 2xN rectangle with samller rectangles of size 1x2, 2x1, and 2x2
# dp[1] = 1
# dp[2] = 3 = 
# dp[3] = 5 = dp[2] + 2 * dp[1]
# dp[4] = 11 = dp[3] + 2 * dp[2]
# dp[5] = 21 = dp[4] + 2 * dp[3]
# dp[6] = 43 = dp[5] + 2 * dp[4]

# dp[i] = dp[i-1] + 2 * dp[i-2]

dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1]) + (2 * dp[i - 2])

print(dp[n] % 10007)