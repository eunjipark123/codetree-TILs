string = input()
# string = "".join(char.lower() for char in string if char.isnumeric() or char.isalpha())

# for char in string:
#     if char.isalpha() or char.isnumeric():
#         print(char.lower(), end = "")


for elem in string:
    if elem >= 'A' and elem <= 'Z':
        print(elem.lower(), end = "")

    elif (elem >= 'a' and elem <= 'z') or (elem >= '0' and elem <= '9'):
        print(elem, end = "")