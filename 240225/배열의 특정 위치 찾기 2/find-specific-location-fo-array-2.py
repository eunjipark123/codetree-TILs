arr = list(map(int, input().split()))

# odds = sum(arr[0:10:2])
# even = sum(arr[1:10:2])

# if odds >= even:
#     print(odds - even)

# else:
#     print(even - odds)

sum_even = 0
sum_odds = 0
for i in range(9):
    if (i + 1) % 2 == 0:
        sum_even += arr[i]
    else:
        sum_odds += arr[i]

print(abs(sum_even - sum_odds))