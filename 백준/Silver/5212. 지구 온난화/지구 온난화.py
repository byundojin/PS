n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]


def f(y, x):
    if arr[y][x] != 'X':
        return None
    result = 0
    if y > 0 and arr[y-1][x]=='X': result += 1
    if y < n-1 and arr[y+1][x]=='X': result += 1
    if x > 0 and arr[y][x-1]=='X': result += 1
    if x < m-1 and arr[y][x+1]=='X': result += 1
    if result >= 2:
        return True
    else:
        return False
    

check_arr = []
for y in range(n):
    check_arr.append([])
    for x in range(m):
        check_arr[y].append(f(y, x))

min_x, min_y = 10, 10
max_x, max_y = 0, 0
for y in range(n):
    for x in range(m):
        if check_arr[y][x]:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        print('X' if check_arr[y][x] else '.', end='')
    print()