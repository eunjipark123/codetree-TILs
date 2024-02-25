# n = int(input())
# cnt = 0
# num = 0
# arr = []


# while cnt < 2:
#     num += n
#     arr.append(num)
#     if num % 5 == 0:
#         cnt += 1

# for i in arr:
#     print(i, end = " ")
    
    


n = int(input())
cnt = 0
arr = []
arr.append(n)

for i in range(1, 10):
    a = arr[i - 1] + arr[0]
    arr.append(a)

for elem in arr:
    print(elem, end = " ")
    if elem % 5 == 0:
        cnt += 1
    if cnt >= 2:
        break