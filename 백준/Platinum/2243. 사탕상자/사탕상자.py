# fenwicktree

import sys
ips = lambda:map(int, sys.stdin.readline().split())

N = 1000000

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

M, *_ = ips()
for _ in range(M):
    ops, *i = ips()
    if ops == 1:
        r = search(*i)
        add(r, -1)
        print(r)
    if ops == 2:
        add(*i)