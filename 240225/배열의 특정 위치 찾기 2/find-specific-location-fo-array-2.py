arr = list(map(int, input().split()))

odds = sum(arr[0:10:2])
even = sum(arr[1:10:2])

if odds >= even:
    print(odds - even)

else:
    print(even - odds)