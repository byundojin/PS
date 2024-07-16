import sys
n = int((ip:=sys.stdin.readline)())
d = {}
for _ in range(n):
    key, value = ip().split()
    key=int(key)
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]
for i in sorted(d.keys()):
    for j in d[i]:
        sys.stdout.write(f"{i} {j}\n")