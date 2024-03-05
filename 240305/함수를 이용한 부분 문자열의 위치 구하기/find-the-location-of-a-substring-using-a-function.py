input_str = input()
target_str = input()


def is_substr(start_idx):
    n, m = len(input_str), len(target_str)

    if start_idx + m - 1 > n:
        return False
    
    for j in range(m):
        if input_str[start_idx + j] != target_str[j]:
            return False

    return True

def find_index():
    n = len(input_str)
    for i in range(n):
        if is_substr(i):
            return i

    return -i        

print(find_index())
# def idx_finder():    
#     idx = -1
#     for i in range(len(input_str)):
#         if input_str[i:i + len(target_str)] == target_str:
#             idx = i
#             break

#     return idx
    

# print(idx_finder())