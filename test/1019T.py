import math

# N = int(input())


def solution(N):
    arr = [0]*10
    parr = []
    k = math.floor(math.log10(N))
    arr[0] -= int("1"*(k+1))
    if N % 10 == 0:
        arr[0] += 1
    while N > 0:
        k = math.floor(math.log10(N))
        k_pow = 10**k
        fn = N // k_pow
        if k > 0:
            for i in range(10):
                arr[i] += (k_pow//10)*k*fn 
        for i in range(fn):
            arr[i] += k_pow
        for i in parr:
            arr[i] += k_pow * fn
        arr[fn] += 1
        parr.append(fn)
        N %= k_pow
        for i in range(k-len(str(N))):
            arr[0] += 1
            parr.append(0)
    return arr


# print(*arr)



file = open("BOJ1019case.txt",'r')
while True:
    line = file.readline().split()
    if not line: break
    result = solution(int(line[0][1:-1]))
    answer = list(map(int, line[1:]))
    if result == answer:
        print("T", line)
    else:
        print("----------------------")
        print("F")
        print(line)
        print(answer)
        print(result)
        print([True if answer[i] == result[i] else False for i in range(10)])
        print("----------------------")