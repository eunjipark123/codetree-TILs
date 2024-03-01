letter = input()
strings = ["apple", "banana", "grape", "blueberry", "orange"]

cnt = 0
# for string in strings:
#     if string[2] == letter or string[3] == letter:
#         print(string)
#         cnt += 1

# print(cnt)

for i in range(5):
    if strings[i][2] == letter or strings[i][3] == letter:
        print(strings[i])
        cnt += 1

print(cnt)