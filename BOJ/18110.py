import sys
import math
N = int(sys.stdin.readline())
if N == 0:
    print(0)
    sys.exit(0)

arr = sorted([int(sys.stdin.readline()) for _ in range(N)])
pn = math.floor((N / 100 * 15) + 0.5)
if pn == 0:
    print(math.floor(sum(arr) / (N - (pn * 2)) + 0.5))
else:
    print(math.floor(sum(arr[pn:-pn]) / (N - (pn * 2)) + 0.5))