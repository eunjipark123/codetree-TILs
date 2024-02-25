arr = list(map(float, input().split()))

avg = sum(arr) / len(arr)

print("{:.1f}".format(avg))