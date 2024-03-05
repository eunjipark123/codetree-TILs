n, m = tuple(map(int, input().split()))
a = [0] + list(map(int, input().split()))

def section_sum_val(m):
    global a
    
    for _ in range(m):
        a1, a2 = tuple(map(int, input().split()))
        print(sum(a[a1:a2+1]))

section_sum_val(m)