n = int(input())
arr = list(map(int, input().split()))

max_profit = 0

for i in range(n):
    for j in range(i, n):
        if arr[j] - arr[i] > max_profit:
            max_profit = arr[j] - arr[i]
    
print(max_profit)