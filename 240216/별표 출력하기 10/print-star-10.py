n = int(input())

# for i in range(1, n + 1):
#     if i % 2 == 1:
#         for _ in range(i // 2 + 1):
#             print("*", end = " ")
#     else:
#         for _ in range(n + 1 - i//2):
#             print("*", end = " ")
#     print()

# for i in range(n, 0, -1):
#     if i % 2 == 1:
#         for _ in range(i // 2 + 1):
#             print("*", end = " ")
#     else:
#         for _ in range(n + 1 - i//2):
#             print("*", end = " ")
#     print()


for i in range(2*n):
    if i % 2 == 0:
        for _ in range(i // 2 + 1):
            print("*", end = " ")
    else:
        for _ in range(n - i//2, 0, -1):
            print("*", end = " ")
    print()