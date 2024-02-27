# 배열 받기 (중간의 엔터는 어떻게 처리...?)
arr_a = [list(map(int, input().split())) for _ in range(3)]
space = input()
arr_b = [list(map(int, input().split())) for _ in range(3)]

# 새로운 배열만들어놓기
arr = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr[i][j] = arr_a[i][j] * arr_b[i][j]

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()