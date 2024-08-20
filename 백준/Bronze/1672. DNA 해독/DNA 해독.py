import sys 
n = int(sys.stdin.readline())
s = list(sys.stdin.readline())
arr = [
    ['A', 'C', 'A', 'G'],
    ['C', 'G', 'T', 'A'],
    ['A', 'T', 'C', 'G'],
    ['G', 'A', 'G', 'T']
]

def idx(c):
    match c:
        case 'A':
            return 0
        case 'G':
            return 1
        case 'C':
            return 2
        case 'T':
            return 3

for i in range(n - 2, -1, -1):
    x, y = idx(s[i]), idx(s[i+1])
    s[i] = arr[x][y]

print(s[0])