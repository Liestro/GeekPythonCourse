# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

import t5_1_logging as t5_1


def file_analyse(file_name):
    """
    Функция возвращает список списков слов

    :return: Возвращает список вида
    [<список слов в первой строке>, <список слов в первой строке>]
    """
    with open(file_name, 'r', encoding='utf-8') as in_file:
        return [i.split() for i in in_file.readlines()]


if __name__ == '__main__':
    # Здесь используется файл, который создается функцией из первого задания
    print('Введите строки \nВведите пустую строку, чтобы закончить ввод')
    file_info = file_analyse(t5_1.input_lines())

    print(f'File has {len(file_info)} lines:')
    for line_c in range(len(file_info)):
        print(f'Line #{line_c + 1} has {len(file_info[line_c])} words;')
