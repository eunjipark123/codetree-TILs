n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        sorted_arr = sorted(arr[:i + 1])
        print(sorted_arr[i // 2], end = " ")

# new_arr = []

# for i in range(n):
#     new_arr.append(arr[i])

#     if i % 2 == 1:
#         continue
#     new_arr.sort()    
    
#     mid = new_arr[(i + 1) // 2]
    
#     print(mid, end = " ")