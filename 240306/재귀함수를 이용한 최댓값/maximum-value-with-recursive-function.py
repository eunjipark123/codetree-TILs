n = int(input())
arr = [0] + list(map(int, input().split()))

def max_calculator(n):
    if n == 0:
        return 0
    
    global arr
    before = max_calculator(n-1)
    if arr[n] >= before:
        return arr[n]
    
    else:
        return before

print(max_calculator(n))