nm = input().split()
n, m = int(nm[0]), int(nm[1])


arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r-1][c-1] = 1 
    
for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()