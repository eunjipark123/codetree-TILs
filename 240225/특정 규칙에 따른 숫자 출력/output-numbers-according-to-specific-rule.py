n = int(input())

cnt = 1

# for i in range(n):
#     for j in range(n):
#         if i > j:
#             print(" ", end = " ")
#         else:
#             print(cnt, end = " ")
#             if cnt < 9:
#                 cnt += 1
#             else:
#                 cnt = 1
#     print()


for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(n - i):
        print(cnt, end = " ")
        cnt += 1
        if cnt == 10:
            cnt = 1
    print()