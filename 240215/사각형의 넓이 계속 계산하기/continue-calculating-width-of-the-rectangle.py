while True:
    arr = input().split()
    w, l, s = int(arr[0]), int(arr[1]), arr[2]

    # 너비 먼저 출력 
    print(f"{w * l}")
    
    # 확인하기
    if s == "C":
        break