for _ in range(int(input())):
    N, M = map(int, input().split())
    if N==M:
        print(1)
        continue

    from pprint import pprint

    arr = [[0]*(M+1) for _ in range(M+1)]
    arr[1] = [1]*(M+1)
    arr[1][0] = 0
    for i in range(1, M):
        for j in range(M):
            arr[i+1][j+1] = arr[i+1][j] + arr[i][j+1]
    print(sum([arr[i][N] for i in range(1, M-N+2)]))