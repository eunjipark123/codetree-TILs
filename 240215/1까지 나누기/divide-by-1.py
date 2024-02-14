n = int(input())
share = n

for i in range(1, n + 1):
    if share // i <= 1:
        print(i)
        break
    share //= i