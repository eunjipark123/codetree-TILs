n = 5

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 1행, 1열에 1 초기화
for j in range(n):
    arr_2d[0][j] = 1
    arr_2d[j][0] = 1

# 바로 위, 왼쪽 값 구하기 
for i in range(1, n):
    for j in range(1, n):
        arr_2d[i][j] = arr_2d[i-1][j] + arr_2d[i][j-1]

# 출력 
for row in arr_2d:
    for elem in row:
        print(elem, end = " ")
    print()