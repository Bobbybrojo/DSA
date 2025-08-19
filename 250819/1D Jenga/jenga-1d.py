n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

s1 -= 1
e1 -= 1
s2 -= 1
e2 -= 1

blocks_a1 = blocks[:s1] + blocks[e1 + 1:]
blocks_a2 = blocks_a1[:s2] + blocks_a1[e2 + 1:]

print(len(blocks_a2))
for b in blocks_a2:
    print(b)

