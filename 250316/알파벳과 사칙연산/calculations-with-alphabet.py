import sys

expression = list(input())

# Calculate the value of the expression given the value of letters
def calc_value(l_vals):
    last_op = ''
    total = 0

    # Perform last operation on total and currrent letter when possible
    for i, v in enumerate(expression):
        if i == 0:
            total = int(l_vals[ord(v) - 97])
        elif i % 2 == 0:
            let_val = l_vals[ord(v) - 97]
            if last_op == '+':
                total += let_val
            elif last_op == '*':
                total *= let_val
            elif last_op == '-':
                total -= let_val
        else:
            last_op = v

    return total
            

# Backtracking sets max_value to 
def backtrack(letter_vals, idx):
    global max_value

    if idx == 6:
        max_value = max(max_value, calc_value(letter_vals))
        return

    # Select number 1-4 for letter val
    for v in range(1, 4 + 1):
        letter_vals[idx] = v
        backtrack(letter_vals, idx + 1)
        letter_vals[idx] = 0

max_value = -sys.maxsize
backtrack([0] * 6, 0)
print(max_value)