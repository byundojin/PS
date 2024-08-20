import sys
for i in map(int, sys.stdin.read().strip().split("\n")):
    print("Y" if i % 6 == 0 else "N")