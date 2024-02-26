# 수열 갯수 값 받기
ab = input().split()
len_a, len_b = int(ab[0]), int(ab[1])

# 수열 a, b 값 받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 원소가 a에 들어있는지 확인하기 위한 flag
in_bool = True
# b의 첫 수열이 포함된 a의 인덱스를 idx_first, 마지막 수열이 포함된 a의 인덱스를 idx_last라고 하면


for i in range(len_b):
    # 들어있지 않다면 연속부분수열일 수 없음
    if b[i] not in a:
        in_bool = False
        break    

if in_bool:
    idx_first = a.index(b[0])
    idx_last = a.index(b[0]) + len_b
    
    idx_b = 0
    b_elem = b[idx_b]
    
    for elem in a[idx_first:idx_last]: 
        if elem != b_elem:
            in_bool = False
            break
        else:
            idx_b += 1
    
    
if in_bool == False:
    print("No")
else:
    print("Yes")