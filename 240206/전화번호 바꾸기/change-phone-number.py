arr = input().split("-")
a = arr[0]
x = int(arr[1])
y = int(arr[2])

x, y = y, x

print(f"{a}-{x}-{y}")