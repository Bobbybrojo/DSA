n = int(input())
num = list(map(int, input().split()))

def backtrack(pos, cnt):
    global min_jump_count

    if pos == n - 1:
        min_jump_count = min(min_jump_count, cnt)
        return

    max_jump_dist = num[pos]
    for i in range(1, max_jump_dist + 1):
        if pos + i >= n:
            break
            
        backtrack(pos + i, cnt + 1)


min_jump_count = n
backtrack(0, 0)
print(min_jump_count if min_jump_count != n else -1)