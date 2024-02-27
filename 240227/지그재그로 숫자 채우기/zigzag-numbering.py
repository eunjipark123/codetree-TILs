nm = input().split()
n, m = int(nm[0]), int(nm[1])

# 포맷은 그대로 둬도 상관없음
arr = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0

for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            arr[i][j] = cnt
        else:
            arr[n-1-i][j] = cnt
        cnt += 1


for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()

# arr_final = [[0 for _ in range(m)] for _ in range(n)]
# for row in arr_final:
#     for elem in row:
#         print(elem, end = " ")
#     print()