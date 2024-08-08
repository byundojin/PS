import sys
n, k = map(int, (ip:=sys.stdin.readline)().split())
arr = [0] * (n+1)
for i in sorted(map(int, ip().split()), reverse=True):
    c = 0
    while i+(k*c) <= n:
        if arr[i+(k*c)] == 0:
            arr[i+(k*c)] = 1
            break
        c += 1
    else:
        print(0)
        exit(0)
print(1)
