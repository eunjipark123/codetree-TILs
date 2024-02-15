n = int(input())

for i in range(n):
    for j in range(n - i):
        a = "*" * (n - i)
        print(a, end = " ")
    print()