arr = input().split()
mid = int(arr[0])
fin = int(arr[1])

if mid >= 90:
    if fin >= 95:
        print(10)
    elif fin >= 10:
        print(5)
else:
    print(0)