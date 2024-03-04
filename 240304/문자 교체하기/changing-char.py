# arr = list(map(list, input().split()))
# arr[1][:2] = arr[0][:2]
# print("".join(arr[1]))


str1, str2 = input().split()

str2 = str1[:2] + str2[2:]

print(str2)