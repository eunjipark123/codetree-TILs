a = input()
def is_palindrome(a):
    if a[::-1] == a:
        return True

    return False 

if is_palindrome(a):
    print('Yes')
else:
    print('No')
# def modify(string):
#     string += "apple"
#     return string

# _str = "banana"
# # _str = modify(_str)

# print(modify(_str))
# print(_str)