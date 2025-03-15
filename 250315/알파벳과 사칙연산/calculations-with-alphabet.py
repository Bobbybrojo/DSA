import sys

expression = [char for char in input()]

# Calculate the value of the expression given the value of letters
def calc_value(l_vals):
    last_op = ''
    total = 0

    # Perform last operation on total and currrent letter when possible
    for i, v in enumerate(expression):
        if i == 0:
            total = int(l_vals[ord(v) - 97])
        elif i % 2 == 0:
            total = eval(f'{str(total)} {last_op} {l_vals[ord(v) - 97]}')
        else:
            last_op = v

    return total
            

# Backtracking sets max_value to 
def backtrack(letter_vals):
    global max_value

    if len(letter_vals) == 6:
        max_value = max(max_value, calc_value(letter_vals))
        return

    # Select number 1-4 for letter val
    for i in range(1, 4 + 1):
        letter_vals.append(i)
        backtrack(letter_vals)
        letter_vals.pop()

max_value = -sys.maxsize
backtrack([])
print(max_value)