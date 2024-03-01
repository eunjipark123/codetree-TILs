arr = input().split()
a, b = arr[0], arr[1]

if len(a) > len(b):
    print(a, len(a))
elif len(a) < len(b):
    print(b, len(b))
else:
    print("same")