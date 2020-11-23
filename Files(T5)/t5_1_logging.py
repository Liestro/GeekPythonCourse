# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

def input_lines(file_name='log.tmp.txt'):
    """
    Функция записывает в файл строки, введенные пользователем до тех пор, пока не будет введена пустая строка

    :param file_name: имя создаваемого файла
    :return: Имя созданного файла
    """
    text_files_dir = 'text_files'
    full_file_name = f'{text_files_dir}\\{file_name}'
    with open(full_file_name, "w", encoding='utf-8') as out_file:
        while True:
            input_string = input('> ')
            if input_string:
                out_file.write(input_string + '\n')
            else:
                break
    return full_file_name


if __name__ == '__main__':
    print('Введите строки \nВведите пустую строку, чтобы закончить ввод')
    input_lines()
