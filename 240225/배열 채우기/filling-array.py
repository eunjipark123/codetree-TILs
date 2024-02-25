arr = list(map(int, input().split()))
arr_lists = []

for i in arr:
    if i == 0:
        break
    else:
        arr_lists.append(i)

for i in arr_lists[::-1]:
    print(i, end = " ")