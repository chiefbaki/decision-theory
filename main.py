import numpy as np
import pandas as pd

columns = ['Варианты решений', 'Цена(-)', 'Удаленность от метро(-)', 'Оборудование(+)', 'Персональные тренеры(+)']


data = [['Alex Fitness', '22000', '480', '8', '9'], ['Физика', '23000', '450', '8', '8'],
        ['Мисс Фитнесс', '24000', '500', '9', '11'],
        ['Фитнесс Холл', '20000', '300', '7', '10'], ['Зебра', '21000', '430', '9', '8'],
        ['X-FIT', '22700', '420', '8', '8'],
        ['We GYM', '18000', '380', '8', '10'], ['Republika', '24000', '320', '7', '9'],
        ['Orange Fitness', '22500', '260', '7', '11'],
        ['Планета Фитнесса', '25000', '192', '9', '10']]

df = pd.DataFrame(data, columns=columns)
df.index = list(range(1, 11))
df.to_csv('data.csv')

file = 'data.csv'
data = pd.read_csv(file, delimiter=',')
alt = data.values.tolist()


def pareto_method(alt):
    result = set()
    for i in range(len(alt)):
        for j in range(len(alt)):
            if i == j:
                continue
            if (alt[i][2] <= alt[j][2]) \
                    and (alt[i][3] <= alt[j][3]) \
                    and (alt[i][4] >= alt[j][4]) \
                    and (alt[i][5] <= alt[j][5]):
                result.add(tuple(alt[i]))
    return result


def upper_bounds():
    '''Верхние границы'''
    u = int(input('Выберите вернхнюю границу: цена(2), удаленность от метро(3), оборудование(4), персональные тренеры(5): '))
    l = int(input('Выберите вернхнюю границу: цена(2), удаленность от метро(3), оборудование(4), персональные тренеры(5): '))
    upper = int(input('Введите верхнюю границу: '))
    lower = int(input('Введите нижнюю границу: '))
    new_list = []

    for i in alt:
        if i[u] <= upper and i[l] >= lower:
            new_list.append(i)

    return pareto_method(new_list)


def sub_opt():
    '''Субоптимизация'''
    cost = int(input('Выберите главный критерий: цена(2), отдаленность от метро(3), оборудование(4), пер. тренеры(5): '))
    criterion = int(input('Введите главный критерий: '))
    o = int(input('Выберите остальные критерии: цена(2), отдаленность от метро(3), оборудование(4), пер. тренеры(5): '))
    oo = int(input('Введите границу критерия:'))
    p = int(input('Выберите остальные критерии: цена(2), отдаленность от метро(3), оборудование(4), пер. тренеры(5): '))
    pp = int(input('Введите границу критерия: '))
    r = int(input('Выберите остальные критерии: цена(2), отдаленность от метро(3), оборудование(4), пер. тренеры(5): '))
    rr = int(input('Введите границу критерия: '))
    new_list = []
    for i in alt:
        if i[o] < oo and i[p] > pp and i[r] > rr:  # 234 2000 120 2
            new_list.append(i)
    for i in new_list:
        if i[cost] < criterion:
            criterion = i[2]
    for i in new_list:
        if i[cost] == criterion:
            print(i)


def lexic_opt():
    '''Лексикографическая оптимизация'''
    m = int(input('Выберите главный критерий:цена(2), отдаленность от метро(3), оборудование(4), пер. тренеры(5): '))
    krit = int(input('Введите верхнюю границу главного критерия: '))
    temp1 = []
    temp2 = []
    for i in alt:
        if i[m] < krit:
            nov.append(i)
    print(nov)
    n = int(input('Выберите второй главный критерий:цена(2), отдаленность от метро(3), оборудование(4), пер. тренеры(5): '))
    krit2 = int(input('Введите верхнюю границу главного критерия: '))
    for i in temp1:
        if i[n] < krit2:
            temp2.append(i)
    print(temp2)


if __name__ == '__main__':
    # pareto method
    # print(alt)
    print(pareto_method(alt))
    # temp = upper_bounds()
    # print(temp)
    #sub_opt()
    #lexic_opt()