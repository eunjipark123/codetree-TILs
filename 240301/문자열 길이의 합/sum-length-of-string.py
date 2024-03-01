n = int(input())
sum_val = 0
cnt = 0 

for _ in range(n):
    a = input()
    sum_val += len(a)
    
    if a[0] == 'a':
        cnt += 1
    
print(sum_val, cnt)