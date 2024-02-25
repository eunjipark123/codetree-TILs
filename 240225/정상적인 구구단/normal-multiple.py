n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == n:
#             print(f"{i} * {j} = {i * j}", end = " ")
#         else:
#             print(f"{i} * {j} = {i * j},", end = " ")
#     print()

# 더 간결하게 만들기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = {i * j}", end = "")
        if j < n:
            print(",", end=" ")
    print()