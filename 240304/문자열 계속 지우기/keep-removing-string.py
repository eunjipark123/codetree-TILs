# 문자열 입력 
a = input()
b = input()
len_a = len(a)
len_b = len(b)


while True:   
    flag = False
    for i in range(len(a)):
        if a[i:i + len_b] == b:            
            flag = True
            a = a[:i] + a[i+len_b:]
                            
    if not flag:
        print(a)
        break