import sys
ips = lambda:map(int, sys.stdin.readline().split())

def sol(N, K, M):
    # Fenwick Tree (1-indexed)
    BIT = [0] * (N + 1)

    def add(i, v):
        while i <= N:
            BIT[i] += v
            i += i & -i

    def search(value):
        # linear v번이 BIT[i]에 속하는 i
        idx = 0
        bit_mask = 1 << (N.bit_length() - 1)
        while bit_mask > 0:
            next_idx = idx + bit_mask
            if next_idx <= N and BIT[next_idx] < value:
                value -= BIT[next_idx]
                idx = next_idx
            bit_mask >>= 1
        return idx + 1

    for i in range(1, N+1):
        add(i, 1)

    p = M
    rm = 0
    rs = N
    for _ in range(N-1):
        # print(BIT)
        idx = search(p-rm)
        # print(rm, rs, idx, p)
        add(idx, -1)
        rm += 1
        p += K
        if rs < p:
            p -= rs
            rs -= rm
            rm = 0
            p %= rs
            if p == 0:
                p = rs

    # print(BIT)
    # print(idx, p)

    print(search(1))

while True:
    N, K, M = ips()
    if not any((N, K, M)):
        exit(0)

    sol(N, K, M)