input_str = input()
target_str = input()


def idx_finder():    
    idx = -1
    for i in range(len(input_str)):
        if input_str[i:i + len(target_str)] == target_str:
            idx = i

    return idx
    

print(idx_finder())