arr = input().split()
a = int(arr[0])
b = int(arr[1])

if a > b:
    results = a * b
else:
    results = b // a

print(results)