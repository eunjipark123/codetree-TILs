# 첫 번째 줄 : n, q
inputs = input().split()
n , q = int(inputs[0]), int(inputs[1])

# 두 번째 줄 : 원소
elements = list(map(int, input().split()))

# 세 번째 줄 : 질의
for _ in range(q):
    quest = list(map(int, input().split()))

    if quest[0] == 1:
        a = quest[1]
        print(elements[a-1])
    
    elif quest[0] == 2:
        a = quest[1]
        if a in elements:
            print(elements.index(a)+1)
        else:
            print(0)
    
    else:
        a, b = quest[1], quest[2]
        for i in range(a - 1, b):
            print(elements[i], end = " ")