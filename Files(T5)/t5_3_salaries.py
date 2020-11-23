# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import t5_2_file_analyse as t5_2
from functools import reduce


def getting_data():
    mode = input('Выберите режим работы:\n'
                 ' i - ввод данных вручную (они все равно запишшутся в файл и считаются оттуда)\n'
                 ' f - Использование данных из готового файла\n'
                 ' Введите что угодно другое для выхода из программы\n> ')

    result = None
    if mode == 'f':
        result = t5_2.file_analyse('text_files\\workers_template.txt')
    elif mode == 'i':
        print('Построчно введите информацию о сотрудниках в формате \n<Фамилия сотрудника> <Величина оклада>\n'
              'Введите пустую строку, чтобы закончить ввод')
        result = t5_2.file_analyse(t5_2.t5_1.input_lines('workers.tmp.txt'))
    return result


def less_than_20(input_data):
    return [i[0] for i in input_data if float(i[1]) < 20000]


def average_income(input_data):
    return sum([float(i[1]) for i in input_data]) / len(input_data)


if __name__ == '__main__':
    data = getting_data()
    if not data:
        exit(0)

    print(less_than_20(data))
    print(average_income(data))
