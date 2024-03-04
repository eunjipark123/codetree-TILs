letter = input()

# print(ord('z')) # 122
# print(ord('a')) # 97

if letter == 'z':
    new_letter = 'a'
else:
    new_letter = chr(ord(letter) + 1)

print(new_letter)