import math

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins_used = 0
target = k
coin_idx = -1

while target != 0:
    coin = coins[coin_idx]
    num_coins = int(target // coin)
    if num_coins >= 1:
        target = target - (num_coins * coin)
        coins_used += num_coins
    else:
        coin_idx -= 1

print(coins_used)