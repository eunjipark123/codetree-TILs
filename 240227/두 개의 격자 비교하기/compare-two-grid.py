# 입력값 받기 
nm = input().split()
n, m = int(nm[0]), int(nm[1])

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

# 행렬 만들기 
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 조건에 맞으면 0, 아님 1
for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            arr[i][j] = 0
        else:
            arr[i][j] = 1

# 출력 
for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()