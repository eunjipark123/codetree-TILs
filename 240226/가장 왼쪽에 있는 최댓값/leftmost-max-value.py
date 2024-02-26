n = int(input())
arr = list(map(int, input().split()))

num = n
while num > 0:
    max_val = 0
    for i in range(num):
        if arr[i] > max_val:
            max_val = arr[i]
            num = i
    print(num + 1, end = " ")