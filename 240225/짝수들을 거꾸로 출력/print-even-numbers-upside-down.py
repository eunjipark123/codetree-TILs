n = int(input())

arr = list(map(int, input().split()))
arr_even = []
for i in arr[::-1]:
    if i % 2 == 0:
        print(i, end = " ")