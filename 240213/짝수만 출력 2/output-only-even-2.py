arr = input().split()
b, a = int(arr[0]), int(arr[1])

#a, b는 짝수임
i = b

while i >= a:
    print(i, end = " ")
    i -= 2