# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

import t5_1_logging as t5_1


def file_analyse(file_name):
    """
    Функция возвращает количество строк и слов в каждойф строке

    :return: Возвращает кортеж вида
    (<количество строк>, [<список слов в первой строке>, <список слов в первой строке>])
    """
    with open(file_name, 'r', encoding='utf-8') as in_file:
        lines = in_file.readlines()

        result2 = (len(lines), [])

        for i in range(len(lines)):
            result2[1].append(lines[i].split())

        return result2


if __name__ == '__main__':
    # Здесь используется файл, который создается функцией из первого задания
    file_info = file_analyse(t5_1.logging())

    print(f'File has {file_info[0]} lines:')
    for line_c in range(len(file_info[1])):
        print(f'Line #{line_c + 1} has {len(file_info[1][line_c])} words;')
