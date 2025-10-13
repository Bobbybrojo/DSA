n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

segments = list(sorted(zip(x1, x2)))


def backtrack(curr, idx):
    global max_segments

    max_segments = max(max_segments, len(curr))
    
    for i in range(idx, len(segments)):
        seg = segments[i]
        
        if len(curr) == 0:
            curr.append(seg)
            backtrack(curr, i + 1)
            curr.pop()
        elif seg[0] > curr[-1][1]:
            curr.append(seg)
            backtrack(curr, i + 1)
            curr.pop()

max_segments = 0
backtrack([], 0)
print(max_segments)