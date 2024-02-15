n = int(input())

# for i in range(n):
#     for _ in range(n - i):
#         print("*", end = " ")
#     print()

# for i in range(n-2, -1, -1):
#     for _ in range(n - i):
#         print("*", end = " ")
#     print()

for i in range(n-1, -1, -1):
    for _ in range(i + 1):
        print("*", end = " ")
    print()

for i in range(1, n):
    for _ in range(i + 1):
        print("*", end = " ")
    print()