arr = list(map(int, input().split()))

# odds = sum(arr[0:10:2])
# even = sum(arr[1:10:2])

# if odds >= even:
#     print(odds - even)

# else:
#     print(even - odds)

sum_even = 0
sum_odds = 0
for i in range(10):
    if i % 2 == 0:
        sum_odds += arr[i]
    else:
        sum_even += arr[i]

if sum_odds >= sum_even:
    print(sum_odds - sum_even)
else:
    print(sum_even - sum_odds)