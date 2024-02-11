arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if a > b:
    if c > a:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
else :
    if a > c:
        print(a)
    elif c > b:
        print(b)
    else:
        print(c)