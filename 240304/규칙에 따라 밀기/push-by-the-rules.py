# string 인풋 받기 
string = input()

# orders 받기
orders = input()


for order in orders:
    if order == "L":
        string = string[1:] + string[0]
    elif order == "R":
        string = string[-1] + string[:-1]

print(string)