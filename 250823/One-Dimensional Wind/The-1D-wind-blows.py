n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def shift_right(row):
    temp = a[row][-1]
    for i in range(m - 1, 0, -1):
        a[row][i] = a[row][i - 1]
    a[row][0] = temp

def shift_left(row):
    temp = a[row][0]
    for i in range(1, m):
        a[row][i - 1] = a[row][i]
    a[row][-1] = temp

def column_match(row1, row2):
    for i in range(m):
        if a[row1][i] == a[row2][i]:
            return True
    return False

def shift_by_direction(row, direction, reverse=False):
    if reverse:
        if direction == 'L':
            shift_left(row)
        else:
            shift_right(row)
    else:
        if direction == 'L':
            shift_right(row)
        else:
            shift_left(row)

for r, d in winds:
    r = r - 1
    # Initial shift
    shift_by_direction(r, d)

    # Upwards propogation
    ur = r - 1
    while ur >= 0:
        if column_match(ur, ur + 1):
            shift_by_direction(ur, d, abs(r - ur) % 2)
            ur -= 1
        else:
            break

    # Downwards propogation
    dr = r + 1
    while dr < n:
        if column_match(dr, dr - 1):
            shift_by_direction(dr, d, abs(r - dr) % 2)
            dr += 1
        else:
            break



# Print answer
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()