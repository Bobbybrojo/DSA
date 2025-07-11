K, N = map(int, input().split())

def choose(curr, n):
    if n == N:
        for elem in curr:
            print(elem, end=" ")
        print()
        return
    
    for i in range(1, K + 1):
        if n < 2 or not (curr[-1] == curr[-2] and curr[-2] == i):
            curr.append(i)
            choose(curr, n + 1)
            curr.pop()

choose([], 0)