n = int(input())
arr = list(map(int, input().split()))
# arr = [2, 3, 3, 1]
max_val = -2**31
sec_max_val = -2**31

for elem in arr:
    if elem > max_val:
        sec_max_val = max_val
        max_val = elem
    
    elif elem == max_val or (elem < max_val and elem > sec_max_val):
        sec_max_val = elem

    
print(max_val, sec_max_val)