from functools import reduce

n, m = map(int, input().split())
A = list(map(int, input().split()))

def find_max_xor(curr, last_idx):
    global max_xor

    if len(curr) == m:
        max_xor = max(max_xor, reduce(lambda x, y: x ^ y, curr))
        return

    for i in range(last_idx + 1, n):
        elem = A[i]
        curr.append(elem)
        find_max_xor(curr, i)
        curr.pop()

max_xor = -1
find_max_xor([], -1)
print(max_xor)