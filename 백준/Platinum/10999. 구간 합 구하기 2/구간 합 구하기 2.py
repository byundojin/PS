import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = [0]
for _ in range(n):
    arr.append(arr[-1] + int(sys.stdin.readline().rstrip()))

upd_log = []
for _ in range(m + k):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    if cmd[0] == 1:
        upd_log.append( (cmd[1], cmd[2], cmd[3]) )
    else:
        ans = arr[cmd[2]] - arr[cmd[1] - 1]
        for l, r, x in upd_log:
            ll = max(l, cmd[1])
            rr = min(r, cmd[2])
            if ll <= rr:
                ans += (rr - ll + 1) * x
        sys.stdout.write(str(ans) + "\n")
