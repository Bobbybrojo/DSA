n = int(input())

count = 0

def backtrack(curr):
    global count
    
    if len(curr) == n:
        count += 1
        return
    if len(curr) > n:
        return

    for i in range(1, 4 + 1):
        curr.extend([i] * i)
        backtrack(curr)
        for _ in range(i):
            curr.pop()

backtrack([])
print(count)