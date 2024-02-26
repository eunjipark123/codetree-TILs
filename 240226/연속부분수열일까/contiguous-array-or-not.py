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
else:
    start_idx = [idx for idx, val in enumerate(a) if val == b[0]]

# 원소 탐색
    for i in start_idx:
        # 길이가 짧으면 넘어감
        if len(a[i:]) < len_b:
            continue
        
        # 두 길이가 같으면 연속부분수열로 인정 -> 바로 yes 치기
        if a[i:i + len_b] == b:
            print("Yes")
            break
    
    # 다 돌려봤는데 이도 저도 아니라면 No
    else:
        print("No")