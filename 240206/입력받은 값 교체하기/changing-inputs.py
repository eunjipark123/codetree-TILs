arr = input().split()
a = int(arr[0])
b = int(arr[1])

# a, b = b, a
temp = a
a = b
b = temp

print(a, b)