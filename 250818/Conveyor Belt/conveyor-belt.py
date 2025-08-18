n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

conveyor = u + d

def rotate_one():
    temp = conveyor[-1]

    for i in range(len(conveyor) - 1, 0, -1):
        conveyor[i] = conveyor[i - 1]

    conveyor[0] = temp

for _ in range(t):
    rotate_one()

top = conveyor[:n]
bot = conveyor[n:]

# Print answer
for elem in top:
    print(elem, end=' ')
print()
for elem in bot:
    print(elem, end=' ')
print()