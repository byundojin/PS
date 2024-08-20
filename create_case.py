import sys
f = open("case_t.txt", "w")
sys.stdout = f
# print(1000,1000,1000)
# arr = [i for i in range(1, 1001)]
# for _ in range(1000):
#     print(1000, *arr)
from itertools import combinations

for n in range(1, 6):
    for m in range(1, 6):
        for k in range(1, n+1):
            print(n, m, k)
            for _ in range(n):
                for i in range(1, m):
                    for comb in combinations(range(1, m+1), i):
                        