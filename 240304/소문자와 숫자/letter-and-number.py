string = input()
string = "".join(char.lower() for char in string if char.isnumeric() or char.isalpha())
print(string)