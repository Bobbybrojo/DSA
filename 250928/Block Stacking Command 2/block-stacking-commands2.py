from collections import defaultdict

n, k = map(int, input().split())
commands = [tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(k)]

block_stacks = defaultdict(int)

for si, ei in commands:
    for i in range(si, ei + 1):
        block_stacks[i] += 1

print(max(block_stacks.values()))
