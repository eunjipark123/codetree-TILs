n = int(input())
arr = list(map(int, input().split()))
min_diff = arr[1] - arr[0]

# for i in arr:
#     for j in arr:
#         if i >= j:
#             continue 
        
#         if j - i < min_diff:
#             min_diff = j - i
        
# print(min_diff)
for i in range(2, n):
    if min_diff > arr[i] - arr[i - 1]:
        min_diff = arr[i] - arr[i - 1]

print(min_diff)