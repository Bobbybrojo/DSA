n = int(input())
blocks = [int(input()) for _ in range(n)]

s1, e1 = map(lambda x: x - 1, map(int, input().split()))
s2, e2 = map(lambda x: x - 1, map(int, input().split()))

blocks = blocks[:s1] + blocks[e1 + 1:]
blocks = blocks[:s2] + blocks[e2 + 1:]

print(len(blocks))
for block in blocks:
    print(block)
