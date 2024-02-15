n = int(input())

# for i in range(n):
#     for _ in range(n - i):
#         a = "*" * (n - i)
#         print(a, end = " ")
#     print()

for i in range(n):
    for _ in range(n - i):
        for _ in range(n - i):
            print("*", end = "")
        print("", end = " ")
    print()