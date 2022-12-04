# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

def num_decomposition(n):
    n_dec = []
    i = 2
    while n > 1:
        if not n % i:
            n_dec.append(i)
            n /= i
        else:
            i += 1
    else:
        n_dec.insert(0, 1)
    return n_dec

n = int(input("Введите число = "))
print(f'Простые множители числа {n} = {num_decomposition(n)}')

