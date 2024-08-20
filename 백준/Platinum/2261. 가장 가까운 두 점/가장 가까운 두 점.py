import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

points.sort(key=lambda x: x[0])


def getDistance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def solution(left, right):
    if left == right:
        return float('inf')
    elif left+1 == right:
        return getDistance(points[left], points[right])

    mid = (left+right)//2
    lv = solution(left, mid)
    rv = solution(mid, right)
    
    minv = min(lv, rv)
    target_points = []
    for i in range(left, right+1):
        if (points[mid][0] - points[i][0])**2 < minv:
            target_points.append(points[i])
    
    target_points.sort(key=lambda x: x[1])
    
    t = len(target_points)
    for i in range(t-1):
        for j in range(i+1, t):
            if (target_points[i][1] - target_points[j][1])**2 < minv:
                minv = min(minv, getDistance(target_points[i], target_points[j]))
            else:
                break
    
    return minv

print(solution(0, n-1))