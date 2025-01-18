def is_prime(func):
    def wrapper(*args):
        result_1 = func(*args)
        if result_1 <= 1:
            return 'Не простое и не составное'
        for i in range(2, result_1):
            if result_1 % i == 0:
                print('Составное')
                return result_1
        print('Простое')
        return result_1
    return wrapper

@is_prime
def sum_three(*args):
    sum_ch = 0
    for i in args:
        sum_ch += i
    return sum_ch

result = sum_three(2, 3, 6)
print(result)
