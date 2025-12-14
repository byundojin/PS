import math
N, K = map(int, input().split())
factorial = math.factorial

r = factorial(N) // (factorial(N-K) * factorial(K))
print(r)