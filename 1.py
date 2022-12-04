# Вычислить число c заданной точностью d

def pi_calc():
    pi = 0
    for i in range(10000):
        pi += (-1)**i / (2*i + 1)
    return 4*pi

d = input('Введите точность d = ')
print(round(pi_calc(), len(d) - 2))