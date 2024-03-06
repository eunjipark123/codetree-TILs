a, b, c = tuple(map(int, input().split()))





def f(n1, n2, n3):
    num = n1 * n2 * n3
    
    # 내부 함수 설정
    def sum_val(n):
        if n < 10:
            return n
        return sum_val(n // 10) + n % 10

    return sum_val(num)

print(f(a, b, c))