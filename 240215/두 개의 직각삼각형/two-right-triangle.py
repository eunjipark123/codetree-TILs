n = int(input())

for i in range(n):
    # 처음 반복 별 만들기 
    for _ in range(n - i):
        print("*", end = "")
    # 빈칸 만들어주고 
    for _ in range(i):
        print(" "*2, end = "")
    # 다시 동일 수만큼 반복
    for _ in range(n - i):
        print("*", end = "")
    print()