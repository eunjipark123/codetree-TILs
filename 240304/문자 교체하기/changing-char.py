arr = list(map(list, input().split()))
arr[1][:2] = arr[0][:2]
print("".join(arr[1]))