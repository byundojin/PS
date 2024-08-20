a, b = input().split()
b = int(b)
result = -1
from itertools import permutations
for i in permutations(list(a), len(a)):
    if i[0] == '0':
        continue
    if b > (ia:=int("".join(i))):
        result = max(result, ia)
print(result)