n = int(input())

# while n >= 1:
#     for j in range(n):
#         print("*", end = " ")
#     print()
#     n -= 1

for i in range(n):
    for _ in range(n-i):
        print("*", end = " ")
    print()