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
    start_idx = [idx for idx in range(len_a) if a[idx] == b[0]]
    
    
    for i in start_idx:
        flags = False

        if len(a[i:]) >= len_b:
            new_a = a[i:i+len_b]
            if new_a == b:
                flags = True
                break    

    if flags:
        print("Yes")
    else:
        print("No")