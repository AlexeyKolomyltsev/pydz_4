import os

path1 = os.path.join('5','file1.txt')
path2 = os.path.join('5','file2.txt')
with open(path1, 'r', encoding="utf-8") as data1:
    l = data1.readline().split()
with open(path2, 'r', encoding="utf-8") as data2:
    k = data2.readline().split()

if l[-3].isdigit() and k[-3].isdigit():         # создаю переменную для целых чисел
    l_num = str(int(l[-3]) + int(k[-3]))
elif not(l[-3].isdigit()) and k[-3].isdigit(): l_num = k[-3]
else: l_num = l[-3]


d={}  #создаю словарь с ключами x в степени и значением коэффициентов
for l_value in l:
    if len(l_value) > 2 and not l_value.isdigit():
        d[l_value[-2:]] = l_value[:-2]
for k_value in k:
    if len(k_value) > 2 and not k_value.isdigit():
        if k_value[-2:] in d:
            d[k_value[-2:]] = str(int(d[k_value[-2:]]) + int(k_value[:-2]))
        else:
            d[k_value[-2:]] = k_value[:-2]

o ='' #создаю строку, в которую помещаю словарь d и переменную l_num
for key in d:
    o += d[key] + key + " + "
o += l_num + " = 0"

path = os.path.join('5','file5.txt')
with open(path, 'a', encoding='utf-8') as my_file:
    my_file.write(o)