n = int(input())
share = n
cnt = 0

for i in range(1, n + 1):
    if share // i <= 1:
        print(cnt)
        break
    share = n // i
    cnt += 1