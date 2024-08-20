import sys
s1 = sys.stdin.readline()
s2 = input()
s1 = s1.replace("0", "")
s1 = s1.replace("1", "")
s1 = s1.replace("2", "")
s1 = s1.replace("3", "")
s1 = s1.replace("4", "")
s1 = s1.replace("5", "")
s1 = s1.replace("6", "")
s1 = s1.replace("7", "")
s1 = s1.replace("8", "")
s1 = s1.replace("9", "")
if s1.find(s2) == -1:
    print(0)
else:
    print(1)