N = int(input())

def print_answer():
    for d in answer:
        print(d, end=" ")
    print()

answer = 0
def backtrack(curr):
    global answer
    if curr == N:
        answer += 1
        return
    if curr > N: 
        return

    for i in range(1, 4 + 1):
        backtrack(curr + i)

backtrack(0)
print(answer)