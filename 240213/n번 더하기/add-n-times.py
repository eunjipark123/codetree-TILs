arr = input().split()
a, n = int(arr[0]), int(arr[1])

# for문으로 푸는 방법
# for _ in range(n):
#     a += n
#     print(a)

# while로 푸는 방법
i = 0
while i < n:
    a += n
    print(a)
    i += 1