n = int(input())

# arr = []
# arr.append(1)
# arr.append(n)

# for i in range(2, 100):
#     if arr[-1] > 100:
#         break
#     arr.append(arr[i - 1] + arr[i - 2])

# for i in arr:
#     print(i, end = " ")
    
arr = [1, n]
cnt = 1

while True:
    cnt += 1
    arr.append(arr[cnt -1] + arr[cnt - 2])
    if arr[cnt] > 100:
        break

for elem in arr:
    print(elem, end = " ")