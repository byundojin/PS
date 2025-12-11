R, M = 31, 1234567891

def hash(string:str):
    r = 0
    for idx, s in enumerate(string):
        i = ord(s) - ord("a") + 1
        r += i * (R**idx)
        r %= M
    print(r)

N = int(input())
hash(input())