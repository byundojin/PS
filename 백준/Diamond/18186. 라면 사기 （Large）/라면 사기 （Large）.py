def solution():
    n, b, c = map(int, input().split())
    arr = list(map(int, input().split()))

    if b <= c:
        return sum(arr) * b 
    
    result = 0
    for i in range(n):
        if arr[i] == 0:
            continue
        result += arr[i] * b
        if i < n - 1 and arr[i + 1] > 0:
            if i < n - 2 and arr[i + 2] > 0:
                if arr[i + 1] > arr[i + 2]:
                    d = min(arr[i], arr[i + 1] - arr[i + 2])
                    arr[i] -= d
                    arr[i + 1] -= d
                    result += d * c
                d = min(arr[i], arr[i + 1], arr[i + 2])
                arr[i + 1] -= d
                arr[i + 2] -= d
                result += d * c * 2
            else:
                d = min(arr[i], arr[i + 1])
                arr[i + 1] -= d
                result += d * c        
    return result           
            
print(solution())