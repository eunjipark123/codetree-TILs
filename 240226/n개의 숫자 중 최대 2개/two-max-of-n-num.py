n = int(input())
arr = list(map(int, input().split()))

max_val = -2**31
sec_max_val = -2**31

for elem in arr:
    if elem == max_val:
        continue

    if elem > max_val:
        sec_max_val = max_val
        max_val = elem
    
    elif elem < max_val and elem > sec_max_val:
        sec_max_val = elem 
    
print(max_val, sec_max_val)