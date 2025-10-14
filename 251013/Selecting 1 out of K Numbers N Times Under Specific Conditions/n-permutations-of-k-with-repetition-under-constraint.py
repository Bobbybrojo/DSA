K, N = map(int, input().split())

def backtrack(curr):
    if len(curr) == N:
        for e in curr:
            print(e, end=' ')
        print()
        return

    for i in range(1, K + 1):
        if len(curr) >= 2 and curr[-2] == curr[-1] and curr[-1] == i:
            continue
        
        curr.append(i)
        backtrack(curr)
        curr.pop()

backtrack([])