import sys
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
house = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 1]
distance = [[abs(i-hi) + abs(j-hj) for hi, hj in house] for i in range(N) for j in range(N) if arr[i][j] == 2]
from itertools import combinations
print(min([sum([min([distance[j][i] for j in comb]) for i in range(len(house))]) for comb in combinations(range(len(distance)), M)]))