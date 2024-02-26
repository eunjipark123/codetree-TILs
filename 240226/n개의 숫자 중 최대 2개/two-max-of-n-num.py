n = int(input())
arr = list(map(int, input().split()))
# 기초적인 방법 : 가장 큰 값을 찾고, 그 값을 제거하고, 나머지에서 가장 큰 값을 찾기
max_val = arr[0]

for elem in arr:
    if elem > max_val:
        max_val = elem

max_idx = arr.index(max_val)        

for i in range(n):
    if i == max_idx:
        arr[i] = -2**31

sec_max_val = arr[0]
for elem in arr:
    if elem > sec_max_val:
        sec_max_val = elem

print(max_val, sec_max_val)