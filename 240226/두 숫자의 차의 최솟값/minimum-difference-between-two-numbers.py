n = int(input())
arr = list(map(int, input().split()))
min_diff = 100

for i in arr:
    for j in arr:
        if i >= j:
            continue 
        
        if j - i < min_diff:
            min_diff = j - i
        
print(min_diff)