import sys
n = int(input())

# Dynamic programmnig problem
# dp[i] represents number of ways to get to the ith floor
# dp[i] = dp[i - 2] if exists + dp[i - 3] if exists


dp = [0 for _ in range(n + 1)]
dp[0] = 0
dp[1] = 0
dp[2] = 1
if n >= 3:
        dp[3] = 1

for i in range(4, n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

print(dp[n] % 10007)