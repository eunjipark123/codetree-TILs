string = input()
len_s = len(string)

for letter in ['ee', 'ab']:
    # exists = False
    
    # for i in range(len_s - 1):
    #     if string[i] == letter[0] and string[i + 1] == letter[1]:
    #         exists = True
        
    # for i in range(len_s - 1):
    #     if string[i:i + 2] == letter:
    #         exists = True
    
    # if exists == True:
    #     print("Yes", end = " ")
    # else:
    #     print("No", end = " ")

    if letter in string:
        print("Yes", end = " ")
    else:
        print("No", end = " ")