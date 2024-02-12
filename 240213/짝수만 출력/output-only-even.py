arr = input().split()
a = int(arr[0])
b = int(arr[1])

i = a

while i <= b:
    # a, b는 짝수만 주어짐
    if i % 2 == 0:
        print(i, end = " ")
    i += 2