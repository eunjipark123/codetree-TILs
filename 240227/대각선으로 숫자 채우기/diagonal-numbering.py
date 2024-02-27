nm = input().split()
n, m  = int(nm[0]), int(nm[1])
arr = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1

for k in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                arr[i][j] = cnt
                cnt += 1


for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()