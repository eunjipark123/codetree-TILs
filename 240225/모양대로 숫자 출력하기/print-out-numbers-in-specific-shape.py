n = int(input())

# for i in range(n):
#     for _ in range(i):
#         print(" ", end = " ")
#     for j in range(n - i, 0, -1):
#         print(j, end = " ")
#     print()
# )

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end = " ")
        else:
            print(j, end = " ")
    print()