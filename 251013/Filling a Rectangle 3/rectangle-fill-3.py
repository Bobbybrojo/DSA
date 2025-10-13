n = int(input())

# dp[i] represnts the number of ways to fill a 2 X N rectangle
# using 1x2, 2x1, and 1x1 rectangles
# dp[i] = dp[i-1]*2 + [i-2]*3 + 2*dp[i - (3, 4, 5... 0)]
# dp[1] = 2
# dp[2] = 7
# dp[3] = 22
# dp[4] = 71

dp = [0 for _ in range(n + 1)]

dp[0] = 1
dp[1] = 2

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] * 2) + (dp[i - 2] * 3)
    for j in range(i - 3, -1, -1):
        dp[i] = dp[i] + (dp[j] * 2)

print(dp[n] % 1000000007)