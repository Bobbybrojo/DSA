K, N = map(int, input().split())

def backtrack(curr):
    if len(curr) == N:
        for elem in curr:
            print(elem, end=" ")
        print(" ")
        return

    for i in range(1, K + 1):
        curr.append(i)
        backtrack(curr)
        curr.pop()

backtrack([])
