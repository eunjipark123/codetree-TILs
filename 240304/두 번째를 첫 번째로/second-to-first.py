string = input()
fst = string[0]
snd = string[1]

# for letter in string:
#     if letter == snd:
#         print(fst, end = "")
#     else:
#         print(letter, end = "")

for i in range(len(string)):
    if string[i] == snd:
        string = string[:i] + fst + string[i + 1:]
        
print(string)