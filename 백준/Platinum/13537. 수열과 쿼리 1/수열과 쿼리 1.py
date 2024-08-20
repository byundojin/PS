import sys,  math
sys.setrecursionlimit(10**6)
n = int((ip:=sys.stdin.readline)())
seg = [None] * (n * 4 + 1)
arr = list(map(int, ip().split()))

def init(n, arr):
    if (l:=len(arr)) == 0:
        return
    if l == 1:
        seg[n] = arr[0]
        return
    seg[n] = sorted(arr)
    m = math.ceil(l / 2)
    init(n*2, arr[:m])
    init(n*2+1, arr[m:])

init(1, arr)

def l_search(arr, n):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] > n: r = m
        else: l = m + 1
    return len(arr) - l
        
def search(n,l,r,i,j,k):
    # print("----------------------")
    # print(n, seg[n])
    # print(l, r, i, j, k)
    if i <= l and r <= j:
        if type(seg[n]) == int:
            return 1 if (seg[n] > k) else 0
        return l_search(seg[n], k)
    if r <= i or j-1 < l:
        return 0
    m = math.ceil((l+r) / 2)
    return search(n*2, l, m, i, j, k) + search(n*2+1, m, r, i, j, k)

q = int(ip())
for _ in range(q):
    i, j, k = map(int, ip().split())
    sys.stdout.write(f"{search(1,0,n,i-1,j,k)}\n")