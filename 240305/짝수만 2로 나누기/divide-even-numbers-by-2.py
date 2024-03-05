n = int(input())
arr = list(map(int, input().split()))

def even_divider(arr):
    for i in range(n):
        if arr[i] % 2 != 0:
            continue
        
        arr[i] //= 2
    
    return arr

for elem in even_divider(arr):
    print(elem, end = " ")

        

# def modify(arr):
#     arr[0] = 10

# _list = [1, 2, 3, 4]
# modify(_list[:])

# for elem in _list:
#     print(elem, end = " ")