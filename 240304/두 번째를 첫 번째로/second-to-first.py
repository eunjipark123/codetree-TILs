string = input()
fst = string[0]
snd = string[1]

for letter in string:
    if letter == snd:
        print(fst, end = "")
    else:
        print(letter, end = "")