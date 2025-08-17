n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for r in range(n - 2):
    for c in range(n - 2):
        num_coins = 0
        for i in range(3):
            for j in range(3):
                if grid[r + i][c + j] == 1:
                    num_coins += 1

        if num_coins > ans:
            ans = num_coins

print(ans)


