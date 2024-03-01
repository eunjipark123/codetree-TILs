arr = input().split()
a, b = arr[0], arr[1]

if len(a) > len(b):
    print(a, len(a))
else:
    print(b, len(b))