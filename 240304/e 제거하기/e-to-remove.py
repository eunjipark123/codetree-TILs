string = input()

# list로 풀기
arr = list(string)
leng = len(arr)

for i in range(leng):
    if arr[i] == 'e':
        arr.pop(i)
        break

string = ''.join(arr)
print(string)
# # slicing으로 풀기 
# for i in range(len(string)):
#     if string[i] == 'e':
#         result = string[:i] + string[i+1:]
#         break

# print(result)