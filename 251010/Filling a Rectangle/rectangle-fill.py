n = int(input())

# Dp[i] represents the number of ways to fill the rectangle
# of size i * 2 with rectangles of size 1x2 and 2x1
# dp[i] = dp[i - 1] + dp[i-2]

dp = [-1 for _ in range(n + 1)]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)