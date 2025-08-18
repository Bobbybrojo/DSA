n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
conveyor = l + r + d

def rotate():
    temp = conveyor[-1]

    for i in range(len(conveyor) - 1, 0, -1):
        conveyor[i] = conveyor[i - 1]

    conveyor[0] = temp

for _ in range(t):
    rotate()

splits = [conveyor[:n], conveyor[n:2*n], conveyor[2*n:]]

for split in splits:
    for elem in split:
        print(elem, end=' ')
    print()

