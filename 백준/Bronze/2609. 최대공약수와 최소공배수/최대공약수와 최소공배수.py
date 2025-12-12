a, b = sorted(map(int, input().split()), reverse=True)

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
    
def lcm(a, b):
    r = gcd(a,b)
    return a*b//r

print(gcd(a, b))
print(lcm(a, b))