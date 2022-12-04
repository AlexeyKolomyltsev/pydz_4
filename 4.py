#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

import random
indexes = {"0": "\u2070",   # создаю словарь для степеней
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           }

def degree(deg):  #функция, добавляющая степени
    degrees = ""
    temp = str(deg)
    for char in temp:
        degrees += indexes[char]
    return degrees

def polonomial(k):  #функция, собирающая многочлен
    polinom = ""
    while k > 0:
        mnozitel = random.randint(0,100)
        if not mnozitel:
            continue
        polinom += str(mnozitel) + 'x' + degree(k) + ' + '
        k -= 1
    else:
        polinom += str(random.randint(0,100)) + " = 0"
    return polinom
    


def create_file(stepen): #функция, записывающая в файл
    with open('file4.txt', 'a', encoding='utf-8') as my_file:
        my_file.write(polonomial(stepen) + "\n")
k = int(input("Введите степеть многочлена "))
create_file(k)