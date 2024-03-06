n = int(input())
arr = list(map(int, input().split()))

def last_common_multiple(n):
    global arr
    
    if n == 1:
        return a[0]

    lastone = last_common_multiple(n-1)
    
    # 새로운 수의 약수
    for i in range(arr[n-1], 0, -1):
        if arr[n-1] % i == 0 and lastone % i == 0:
            return lastone // i * arr[n-1] 

        
print(last_common_multiple(n))