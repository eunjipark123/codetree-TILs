n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1

for i in range(n):
    for j in range(n):
        arr[j][i] = cnt
        cnt += 1

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()

# n = 4

# arr = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]

# cnt = 1

# for i in range(n):
#     for j in range(n):
#         if i % 2 == 0:
#             arr[i][j] = cnt
#         else:
#             arr[i][n-1-j] = cnt
#         cnt += 1

# for row in arr:
#     for elem in row:
#         print(elem, end = " ")
#     print()