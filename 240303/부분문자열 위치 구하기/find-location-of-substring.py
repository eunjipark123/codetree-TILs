input_string = input()
target_string = input()

len_i = len(input_string)
len_t = len(target_string)


if target_string in input_string:
    print(input_string.index(target_string))
else:
    print(-1)