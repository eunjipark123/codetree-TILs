# 문제
string = input()

for i in string:
    if not i.isalpha():
        continue
    
    print(i.upper(), end = "")



# 개념
# letter = 'X'

# # new_letter = chr(ord(letter) - ord('A') + ord('a'))
# # print(new_letter)

# # lower_next_letter = chr(ord(letter) + 1).lower()
# # print(lower_next_letter)

# # lower_next_letter = chr(ord(letter) + 1 - ord('A') + ord('a'))
# # print(lower_next_letter)

# x = 'B'
# if x >= 'A' and x <= 'Z':
#     print("Upper Case")