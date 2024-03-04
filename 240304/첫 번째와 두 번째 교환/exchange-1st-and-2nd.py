string = input()
fst_letter = string[0]
scd_letter = string[1]

for letter in string:
    if letter == fst_letter:
        print(scd_letter, end = "")
    elif letter == scd_letter:
        print(fst_letter, end = "")
    else:
        print(letter, end = "")