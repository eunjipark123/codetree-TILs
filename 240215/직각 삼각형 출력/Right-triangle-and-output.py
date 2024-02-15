n = int(input())

# for i in range(1, n + 1):
#     i = 2 * i - 1
#     for _ in range(i):
#         print("*", end = "")
#     print()

for i in range(n):
    for _ in range(2 * i + 1):
        print("*", end = "")
    print()