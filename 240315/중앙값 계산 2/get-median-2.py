n = int(input())
arr = list(map(int, input().split()))
new_arr = []

for i in range(n):
    new_arr.append(arr[i])

    if i % 2 == 1:
        continue
    new_arr.sort()    
    
    mid = new_arr[(i + 1) // 2]
    
    print(mid, end = " ")