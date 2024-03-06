n = int(input())
arr = [0] + list(map(int, input().split()))

def max_calculator(n):
    if n == 0:
        return 0
    
    global arr
    if arr[n] >= max_calculator(n-1):
        return arr[n]
    
    else:
        return max_calculator(n-1)

print(max_calculator(n))