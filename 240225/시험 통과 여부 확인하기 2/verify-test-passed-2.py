n = int(input())
num_stuments = 0

for student in range(n):
    scores = list(map(int, input().split()))
    sum_val = 0
    cnt = 0

    for score in scores:
        sum_val += score
        cnt += 1

    avg = sum_val / cnt

    if avg >= 60:
        print("pass")
        num_stuments += 1
    
    else:
        print("fail")

    
print(num_stuments)