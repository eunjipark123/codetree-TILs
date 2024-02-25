n = int(input())

arr = []
arr.append(1)
arr.append(n)

for i in range(2, 100):
    if arr[-1] > 100:
        break
    arr.append(arr[i - 1] + arr[i - 2])

for i in arr:
    print(i, end = " ")