n = int(input())
arr = list(map(int, input().split()))

arr_new = [i for i in arr if i % 2 == 0]

for i in arr_new:
    print(i, end = " ")