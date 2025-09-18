N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

stack = []
for i in range(len(command)):
    cmd = command[i]
    val = num[i]
    if cmd == "push_back":
        stack.append(val)
    if cmd == "get":
        print(stack[val - 1])
    if cmd == "size":
        print(len(stack))
    if cmd == "pop_back":
        stack.pop()