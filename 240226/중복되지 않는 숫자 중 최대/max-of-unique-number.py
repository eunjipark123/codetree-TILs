n = int(input())
arr = list(map(int, input().split()))

# n = 7
# arr = [3, 2, 3, 4, 5, 5, 1]
max_val = 0
dup_idx = []

while True:
    if max_val != 0:
        break
    elif len(dup_idx) == n:
        max_val = -1
    
    for i in range(n):
        # 제낄 조건 : 수가 작거나 중복리스트에 들어간 경우
        if arr[i] < max_val:
            continue
        
        if i in dup_idx:
            continue

        # 큰 수가 처음 나오면
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = []
            max_idx.append(i)
        
        # 같은 수가 나오면
        elif arr[i] == max_val:
            max_idx.append(i)
            max_val = 0
            
            for idx in max_idx:
                dup_idx.append(idx)
            break
        
print(max_val)