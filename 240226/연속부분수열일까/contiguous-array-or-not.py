# a, b 길이값 받기
ab = input().split()
len_a, len_b = int(ab[0]), int(ab[1])

# 수열 a, b 값 받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# b의 처음 원소가 a에 있는지 확인 -> 없다면 No
if b[0] not in a:
    print("No")

# 있다면 해당 원소가 있는 a의 위치를 찾음
start_idx = []
else:
    start_idx = [idx for idx in range(len_a) if a[idx] == b[0]]
    
    
    for i in start_idx:
        # 그 위치부터의 원소의 갯수를 세서, b의 원소 갯수보다 적다면 무조건 탈락
        if len(a[i:]) < len_b:
            print("No")
            break

        # 아니라면 a를 해당 길이만큼 슬라이싱해서 두 배열이 같은지 Flag로 확인            
        new_a = a[i:i+len_b]
        flags = False
        
        if new_a == b:
            flags = True
            break

    if flags:
        print("Yes")
    else:
        print("No")
        
            


        
    # if in_bool == False:
    #     print("No")
    # else:
    #     print("Yes")
    # test
# len_a, len_b = 13, 6
# a = [1, 2, 5, 2, 5, 2, 3, 2, 5, 2, 5, 2, 5]
# b = [2, 5, 2, 5, 2, 5]