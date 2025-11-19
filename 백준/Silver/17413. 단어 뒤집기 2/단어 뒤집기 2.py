from collections import deque
s = input()

t = ""
g = False
for i in s:
    if i == "<":
        first = True
        for j in t.split():
            if not first:
                print(end=" ")
            first = False
            for k in reversed(j):
                print(k, end="")
        t = ""
        g = True
    t = f"{t}{i}"
    if i == ">":
        print(t, end="")
        g = False
        t = ""

first = True
for j in t.split():
    if not first:
        print(end=" ")
    first = False
    for k in reversed(j):
        print(k, end="")