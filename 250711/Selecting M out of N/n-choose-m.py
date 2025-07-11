N, M = map(int, input().split())

curr = []
def combinations(cnt, last_num):
    if cnt == M:
        for elem in curr:
            print(elem, end=" ")
        print()
        return

    for n in range(last_num, N + 1):
        curr.append(n)
        combinations(cnt + 1, n + 1)
        curr.pop()

combinations(0, 1)

