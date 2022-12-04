# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def exclusiv_n(arr):
    excl_array = []
    dublicate_n = []
    while len(arr) > 0:
        tmp_n = arr.pop(0)
        if tmp_n not in arr \
             and tmp_n not in excl_array \
                and tmp_n not in dublicate_n:
            excl_array.append(tmp_n)
        else:
            dublicate_n.append(tmp_n)
    return excl_array

a = [1, 1, 2, 3, 4, 4, 4]
print(exclusiv_n(a))
