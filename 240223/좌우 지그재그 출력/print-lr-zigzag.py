n = int(input())

# for i in range(n):
#     if i % 2 == 0:
#         cnt_0 = n * i + 1
#         for _ in range(n):
#             print(cnt_0, end = " ")
#             cnt_0 += 1
#     else:
#         cnt_1 = n * (i + 1)
#         for _ in range(n):
#             print(cnt_1, end = " ")
#             cnt_1 -= 1
#     print()


for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(i * n + j + 1, end = " ")
        else:
            print(n * (i + 1) - j, end = " ")
    print()