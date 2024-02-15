# for i in range(6):
#     if i % 2 == 0:
#         for _ in range(i + 1):
#             print("*", end = "")
#         print()
#     else:
#         print("$")

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 1:
        print("*")
    else:
        for _ in range(i):
            print("*", end = " ")
        print()