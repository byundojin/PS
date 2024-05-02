import sys
from pprint import pprint
ip = sys.stdin.readline
sys.setrecursionlimit(10**9)
T = int(ip())
for _ in range(T):
    M, N, K = map(int, ip().split())
    arr = [[False]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, ip().split())
        arr[y][x] = True
    
    pprint(arr)

    def dfs(x, y):
        if not arr[y][x]:
            return False
        arr[y][x] = False
        if x > 0:
            dfs(x-1, y)
        if x < M-1:
            dfs(x+1, y)
        if y > 0:
            dfs(x, y-1)
        if y < N-1:
            dfs(x, y+1)
        return True
    
    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(j, i):
                result += 1

    print(result)