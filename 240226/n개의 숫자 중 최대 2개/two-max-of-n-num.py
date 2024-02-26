# 값을 받고
n = int(input())
arr = list(map(int, input().split()))

# 가장 낮은 값을 설정
max_val = -2**31
sec_max_val = -2**31

# 최고값과 두 번째 값을 업데이트
for elem in arr:
    # case1 : max_val, sec_max_val 모두 업데이트 하는 경우
    if elem >= max_val:
        sec_max_val = max_val # 물려주고
        max_val = elem # 최대값 반영
    
    # case2 : sec_max_val만 업데이트 하는 경우 (최대값이 두 번 이상 반복되면, sec_val도 max_value와 동일)
    elif elem > sec_max_val:
        sec_max_val = elem

    
print(max_val, sec_max_val)