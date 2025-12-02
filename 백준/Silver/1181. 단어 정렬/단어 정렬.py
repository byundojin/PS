N = int(input())

li = list(set((input() for _ in range(N))))
li.sort()
li.sort(key=lambda x:len(x))

for i in li:
    print(i)