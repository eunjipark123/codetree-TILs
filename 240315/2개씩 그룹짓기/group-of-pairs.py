n = int(input()) * 2
arr = list(map(int, input().split()))

# 숫자가 작은 순으로 정렬
arr.sort()

# 빈 리스트 생성
new_arr = []

# 배열을 돌면서 남은 수 중 가장 작은 수와 가장 큰 수의 합을 구함 
for i in range(n):
    new_arr.append(arr[i] + arr[n-1-i])

# 합계가 가장 큰 경우를 선택 
print(max(new_arr))