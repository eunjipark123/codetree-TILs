num_a, num_b = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_continuous_partial_sequence(num_a, num_b, a, b):
    for i in range(num_a - num_b):
        if a[i:i + num_b] == b:
            return True
            break
    
    return False


print('Yes') if is_continuous_partial_sequence(num_a, num_b, a, b) else print('No')