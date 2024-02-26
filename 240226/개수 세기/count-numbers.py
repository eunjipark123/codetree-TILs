arr = input().split()
n, m = int(arr[0]), int(arr[1])

numbers = list(map(int, input().split()))

# print(numbers.count(m))

cnt = 0
for i in numbers:
    if i == m:
        cnt += 1

print(cnt)



# word = ['A', 'P', 'P', 'L', 'E']

# cnt = 0
# for char in word:
#     if char == 'P':
#         cnt += 1

# print(cnt)

# cnts = word.count('P')
# print(cnts)