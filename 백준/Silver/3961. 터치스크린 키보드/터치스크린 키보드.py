import sys 

keyboard = ["qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
]
kdict = {}
for i in range(len(keyboard)):
    for j in range(len(keyboard[i])):
        kdict[keyboard[i][j]] = (i, j)

def f(s: str):
    return [kdict[i] for i in s]

def gap(s1, s2):
    r = 0
    for i in range(len(s1)):
        x1, y1 = s1[i]
        x2, y2 = s2[i]
        r += abs(x1 - x2) + abs(y1-y2)
    return r

n = int(sys.stdin.readline())
for _ in range(n):
    string, m = sys.stdin.readline().split()
    m = int(m)
    strlist = f(string)
    r = []
    for i in range(m):
        s = sys.stdin.readline().rstrip()
        slist = f(s)
        r.append((gap(slist, strlist), s))
    r.sort()
    for i in r:
        print(i[1], i[0])
