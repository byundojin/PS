import sys
from dataclasses import dataclass 
N = int(sys.stdin.readline())

@dataclass 
class Pipe:
    point:int
    capa:int
    flow:int = 0

def get_index(chr:str) -> int:
    if chr.isupper():
        return ord(chr) - ord("A")
    else:
        return ord(chr) - ord('a') + 26

graph:list[list[Pipe]] = [[None]*52 for _ in range(52)]

for _ in range(N):
    pointA, pointB, capa = sys.stdin.readline().split()
    pointA = get_index(pointA)
    pointB = get_index(pointB)
    capa = int(capa)
    if graph[pointA][pointB]:
        graph[pointA][pointB].capa += capa
    else:
        graph[pointA][pointB] = Pipe(pointB, capa)
    if graph[pointB][pointA]:
        graph[pointB][pointA].capa += capa
    else:
        graph[pointB][pointA] = Pipe(pointA, capa)

source = 0
sink = 25
MAX_CAPA = 1000

def DFS(n, load:list[int]=[]):
    if n == source and load != []:
        return 0
    
    if n == sink:
        load += [sink]
        min_capa = MAX_CAPA
        for i in range(len(load)-1):
            if graph[load[i]][load[i+1]].flow > 0:
                min_capa = min(min_capa, graph[load[i]][load[i+1]].capa - graph[load[i]][load[i+1]].flow)
            else:
                min_capa = min(min_capa, graph[load[i]][load[i+1]].capa + graph[load[i+1]][load[i]].flow)
        for i in range(len(load)-1):
            if graph[load[i]][load[i+1]].flow > 0:
                graph[load[i]][load[i+1]].flow += min_capa
            else:
                if min_capa > graph[load[i+1]][load[i]].flow:
                    graph[load[i]][load[i+1]].flow += min_capa - graph[load[i+1]][load[i]].flow
                    graph[load[i+1]][load[i]].flow = 0
                else:
                    graph[load[i+1]][load[i]].flow -= min_capa

    for i in graph[n]:
        if i == None:
            continue
        if i.point in load:
            continue
        if graph[n][i.point].capa - graph[n][i.point].flow == 0:
            continue
        DFS(i.point, load+[n])

DFS(source)

result = 0
for i in range(52):
    if graph[sink][i]:
        result += graph[i][sink].flow
print(result)