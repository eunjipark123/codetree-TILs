n = int(input())

# for i in range(1, n + 1):
#     for j in range(i):
#         print(j + 1, end = "")
#     print()

for i in range(n):
    for j in range(i + 1):
        print(j + 1, end = " ")
    print()