nm = input().split()
n, m = int(nm[0]), int(nm[1])

arr = [[0 for _ in range(n)] for _ in range(m)]
cnt = 0

for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            arr[j][i] = cnt
        else:
            arr[j][n-1-i] = cnt
        cnt += 1


arr_final = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(arr[j][i], end = " ")
    print()

# for row in arr_final:
#     for elem in row:
#         print(elem, end = " ")
#     print()