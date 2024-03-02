arr = input().split()
string, letter = arr[0], arr[1]
len_s = len(string)

#  반복문으로 풀 때
# start_idx = -1
# for i in range(len_s):
#     if string[i] == letter:
#         start_idx = i
#         break

# print(start_idx) if start_idx != -1 else print("No")

# index로 풀 때 
# if letter in string:
#     print(string.index(letter))
# else:
#     print("No")

# find로 풀 때
if letter in string:
    print(string.find(letter))
else:
    print("No")