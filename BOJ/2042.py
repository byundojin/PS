import sys

N, M, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0] * (N * 4)
def init(n=1, l=0, r=N-1):
    if l == r:
        tree[n] = arr[l]
        return tree[n]
    else:
        tree[n] = init(n*2, l, (l+r)//2) + init(n*2+1, (l+r)//2+1, r)
        return tree[n]
        
init()

def update(node, start, end, index, diff) :
 
    if index < start or index > end :
        return
 
    tree[node] += diff
    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)
    
def subSum(node, start, end, left, right) :  
    if left > end or right < start :
        return 0

    if left <= start and end <= right :
        return tree[node]

    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2 + 1, (start+end)//2+1, end, left, right)
 

for _ in range(M+K) :
    a, b, c = map(int, input().rstrip().split())
    if a == 1 :
        b = b-1
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, N-1, b, diff)
    elif a == 2 :                
        print(subSum(1, 0, N-1 ,b-1, c-1))
 