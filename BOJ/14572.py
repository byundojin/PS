import sys

N, K, D = map(int, sys.stdin.readline().split())
result = 0
effort = {}
student_num = {}
for _ in range(N):
    _, d = map(int, sys.stdin.readline().split())
    if d in effort:
        student_num[d] += 1
    else:
        effort[d] = [0] * K
        student_num[d] = 1
    for i in map(int, sys.stdin.readline().split()):
        effort[d][i - 1] += 1

effort_key = sorted(effort.keys())
student = 0
min_key = 0
alg = [0] * K
# print(effort)
# print(student_num)
for i in range(len(effort_key)):
    # print("==============")
    while effort_key[i] - effort_key[min_key] > D:
        for j in range(K):
            alg[j] -= effort[effort_key[min_key]][j]
        student -= student_num[effort_key[min_key]]
        min_key += 1
    inter_count = 0
    union_count = 0

    student += student_num[effort_key[i]]
    for j in range(K):
        alg[j] += effort[effort_key[i]][j]
        if alg[j] > 0:
            union_count += 1
            if alg[j] == student:
                inter_count += 1
    # print(alg)

    result = max((union_count - inter_count) * student, result)

print(result)    
