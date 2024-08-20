import sys
s = sys.stdin.read()
while s.find("BUG") != -1:
    s = s.replace("BUG", "", -1)
sys.stdout.write(s)