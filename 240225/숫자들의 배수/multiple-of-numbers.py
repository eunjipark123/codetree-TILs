n = int(input())
cnt = 0
num = 0
arr = []


while cnt < 2:
    num += n
    arr.append(num)
    if num % 5 == 0:
        cnt += 1

for i in arr:
    print(i, end = " ")