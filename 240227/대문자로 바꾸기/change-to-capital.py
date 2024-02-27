arr_2d = [
    input().split() for _ in range(5)
]

for i in range(5):
    for j in range(3):
        arr_2d[i][j] = chr(ord(arr_2d[i][j]) - ord('a') + ord('A'))
        print(arr_2d[i][j], end = " ")
    print()






# # n = 5

# # b = ([list(input().split()) for _ in range(n)])

# # for row in b:
# #     for i in row:
# #         print(chr(ord(i) + (ord('A') - ord('a'))), end = " ")
# #     print()

# arr_2d = [
# 	list(input().split())
# 	for _ in range(5)
# ]

# for i in range(5):
#     for j in range(3):
#         arr_2d[i][j] = chr(ord(arr_2d[i][j]) + ord('A') - ord('a'))
#         print(arr_2d[i][j], end = " ")
#     print()