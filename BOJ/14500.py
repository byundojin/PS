import sys
N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def dfs(x, y, dep = 1, back=0, t = False):
    if dep == 4:
        return arr[y][x]
        
    result = 0
    if dep == 2:
        if back < 3 and 0 < y < N - 1:
                result = max(result, arr[y-1][x] + arr[y+1][x])
        if back > 2 and 0 < x < M - 1:
                result = max(result, arr[y][x-1] + arr[y][x+1])
    if x > 0 and back != 1:
        result = max(result, dfs(x-1, y, dep+1, 2))
    if x+1 < M and back != 2:
        result = max(result, dfs(x+1, y, dep+1, 1))
    if y > 0 and back != 3:
        result = max(result, dfs(x, y-1, dep+1, 4))
    if y+1 < N and back != 4:
        result = max(result, dfs(x, y+1, dep+1, 3))
    return result + arr[y][x]

r = 0
for i in range(N):
    for j in range(M):
        r = max(r, dfs(j, i))
print(r)