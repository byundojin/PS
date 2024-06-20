import sys
import math
r = sys.stdin.readline
N = int(r())
arr = [0] * 3000000
black = list(map(int,r().split()))
gray = list(map(int,r().split()))
white = list(map(int,r().split()))
for i in range(N):
    arr[black[i]] += 1
    arr[black[i] + gray[i]] += 3
    arr[black[i] + gray[i] + white[i]] += -5
arr[0] += N
c = 0
while arr[c]:
    c += 1
    if c > 3000000:
        break
    arr[c] += arr[c - 1]

black = None
gray = None
white = None

M = int(r())

tree = [0] * 1200_0000

def init(node, start, end):
    if start == end:
        tree[node] = 1
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]
    
init(1,0, 3000000-1)

def q(n, t, l, r):
    tree[n] -= 1
    if l == r:
        return l
    m = (l + r) // 2
    if tree[n*2] >= t:
        return q(n*2,t, l, m)
    else:
        return q(n*2+1,t - tree[n * 2], m + 1, r)
    
for i in map(int,r().split()):
    print(arr[q(1, i, 1, 3000000) - 1])