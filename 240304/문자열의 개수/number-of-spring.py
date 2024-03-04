cnt = 0
arr = []

while True:
    string = input()
    if string == '0':
        break
    else:
        cnt += 1
        arr.append(string)
    
print(cnt)
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])