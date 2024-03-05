n = int(input())
arr = list(map(int, input().split()))

def abs_maker(arr):
    for i in range(len(arr)):
        if arr[i] >= 0:
            continue
        
        arr[i] = arr[i] * (-1)


abs_maker(arr)
for elem in arr:
    print(elem, end = " ")