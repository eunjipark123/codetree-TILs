string = input()
# string = "".join(char.lower() for char in string if char.isnumeric() or char.isalpha())

for char in string:
    if char.isalpha() or char.isnumeric():
        print(char.lower(), end = "")