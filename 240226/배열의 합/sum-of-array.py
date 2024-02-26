n = 4

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# for row in arr:
#     sum_val = 0
#     for i in row:
#         sum_val += i
    
#     print(sum_val)


for i in range(4):
    print(sum(arr[i]))