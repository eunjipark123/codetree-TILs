n = int(input())

for _ in range(n):
    arr = input().split()
    mul = 1
    a, b = int(arr[0]), int(arr[1])

    for i in range(a, b + 1):
        mul *= i
    
    print(mul)