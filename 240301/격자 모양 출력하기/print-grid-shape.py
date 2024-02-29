nm = input().split()
n, m = int(nm[0]), int(nm[1])

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))

    for _ in range(n):
        for _ in range(n):
            arr[r-1][c-1] = r * c


for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()