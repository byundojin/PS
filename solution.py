import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(3000)
sys.stdin = open("case_t.txt", "r")
ip = sys.stdin.readline
sys.stdout = open("answer.txt", "w")

def solution():
    N, M, K = map(int, ip().split())
    SOURCE = "s"
    SINK = "t"
    ORIGIN = "o"
    REPLICA = "r"
    print(N, M, K)

    graph:dict[str, dict[str, int]] = {}
    graph[SOURCE] = {ORIGIN:N, REPLICA:N}
    graph[ORIGIN] = {}
    graph[REPLICA] = {}
    graph[SINK] = {}
    for i in range(1, N+1):
        worker = f"w{i}"
        graph[ORIGIN][worker] = 1
        graph[REPLICA][worker] = 1
        graph[worker] = {}
        _, *opers = map(int, ip().split())
        print(len(opers), *opers)
        for j in opers:
            oper = f"o{j}"
            graph[worker][oper] = 1

    for i in range(1, M+1):
        oper = f"o{i}"
        graph[oper] = {SINK:1} 



    from pprint import pprint
    # print("===============")
    # pprint(level)
    # print("---------------")
    # pprint(graph)
    # print("===============")


    is_sink_o = True
    c = 1
    while is_sink_o:
        level = {}
        def get_level():
            queue = deque()
            def _get_level(node=SOURCE, deps=0):
                if node in level:
                    return
                level[node] = deps
                for n in graph[node]:
                    queue.append((n, deps+1))

            _get_level()
            while queue:
                _get_level(*queue.popleft())

        get_level()


        path = deque()
        r_path = deque()

        def dfs(node=SOURCE, capa=N*2):
            is_sink = False
            path.append(node)
            if node == SINK:
                for i in range(len(path)-1):
                    p = path[i]
                    n = path[i+1]
                    graph[p][n]-=1
                r_path.append(path.copy())
                is_sink = True
            else:
                is_sink = False
                for n in graph[node].copy():
                    if n in path:
                        continue
                    if graph[node][n] == 0:
                        continue
                    if level[node]+1 != level[n]:
                        continue
                    if capa:
                        if p_sink:=dfs(n, graph[node][n]):
                            capa -= 1
                        is_sink = is_sink or p_sink
            path.pop()
            return is_sink

        is_sink_o = dfs()
        

        while r_path:
            p_path = r_path.pop()
            for i in range(len(p_path)-1):
                p = p_path[i]
                n = p_path[i+1]
                if n in graph[p] and graph[p][n] == 0:
                    graph[p].pop(n)
                if p in graph[n]:
                    graph[n][p] += 1
                else:
                    graph[n][p] = 1
        
        c+=1
    print("-------------------")
    print(len(graph[SINK]))

while True:
    try:
        print("===================")
        solution()
        print("===================")
    except EOFError:
        break

"""
5 5 1
3 1 2 3
1 1
1 5
1 5
1 5
"""