import sys
ips = lambda:map(int, sys.stdin.readline().split())

T, *_ = ips()
for _ in range(T):
    a, b = ips()

    check = []

    res = 1
    for _ in range(b):
        res = (res*a)%10
        if res in check:
            break
        check.append(res)
    else:
        if res == 0:
            res = 10
        print(res)
        continue

    res = check[b%len(check)-1]
    if res == 0:
        res = 10
    print(res)
