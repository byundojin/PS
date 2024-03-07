import sys

# N = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))

N = 100000
arr = list(range(100000))
tree = [0] * (N * 4)

def init(n=1, l=0, r=N-1):
    if l == r:
        tree[n] = arr[l]
        return [tree[n]]
    else:
        tree[n] = sorted(init(n*2, l, (l+r)//2) + init(n*2+1, (l+r)//2+1, r))
        return tree[n]

init()

def subSum(node, start, end, left, right, t):
    if left > end or right < start :
        return 0

    if left <= start and end <= right :
        return search(tree[node], t)
    
    return subSum(node*2, start, (start+end)//2, left, right, t) + subSum(node*2 + 1, (start+end)//2+1, end, left, right, t)

def search(l, t):
    if type(l) != list:
        if l > t:
            return 1
        else:
            return 0
    elif len(l) == 1:
        if l[0] > t:
            return 1
        else:
            return 0
    elif len(l) == 0:
        return 0
    elif l[len(l)//2] > t:
        return search(l[:len(l)//2], t) + len(l)-(len(l)//2)
    else :
        return search(l[len(l)//2+1:], t) 
    
# M = int(sys.stdin.readline())
M = 100000

for _ in range(M):
    # a, b, c = map(int, input().rstrip().split())
    a, b, c = 1, 100000, 1
    sys.stdout.write(f"{subSum(1, 0, N-1 ,a-1, b-1, c)}\n")