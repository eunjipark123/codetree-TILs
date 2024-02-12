arr = input().split()
a = int(arr[0])
b = int(arr[1])

# a, b 모두 홀수가 입력되므로 다른 조건은 무시
for i in range(a, b+1, 2):
    print(i, end = " ")