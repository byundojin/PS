import sys,  math
s=1
l=10
p=None
togle = True
for i in sys.stdin.read().split('\n'):
  if i == '0':
    exit(0)
  if togle:
    togle=False
    p = int(i)
  else:
    togle=True
    if i == "too high":
      l = min(p-1, l)
    elif i == "too low":
      s = max(p+1, s)
    else:
      if s<=p<=l:
        print("Stan may be honest")
      else:
        print("Stan is dishonest")
      s=1
      l=10
      p=None
      togle = True