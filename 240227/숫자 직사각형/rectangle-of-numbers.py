nm = input().split()
n, m = int(nm[0]), int(nm[1])

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1

for row in arr:
    for elem in row:
        print(num, end = " ")
        num += 1
    print()






# n = 4
# m = 2
# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]

# # for i in range(n):
# #     for j in range(n):
# #         print(arr_2d[i][j], end = " ")
# #     print()

# # for row in arr_2d:
# #     for elem in row:
# #         print(elem, end = " ")
# #     print()

# n = 3
# arr_2d = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]

# num = 1
# for i in range(n):
#     for j in range(n):
#         arr_2d[i][j] = num
#         num += 2

# for row in arr_2d:
#     for elem in row:
#         print(elem, end = " ")
#     print()