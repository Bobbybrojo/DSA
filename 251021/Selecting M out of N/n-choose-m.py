N, M = map(int, input().split())

def combinations(curr, last_idx):
    if len(curr) == M:
        for elem in curr:
            print(elem, end=" ")
        print()
        return

    for i in range(last_idx + 1, N + 1):
        curr.append(i)
        combinations(curr, i)
        curr.pop()

combinations([], 0)