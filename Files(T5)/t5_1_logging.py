# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

def logging():
    """
    Функция записывает в файл строки, введенные пользователем до тех пор, пока не будет введена пустая строка

    :return: Имя созданного файла
    """
    file_name = 'log.txt'
    with open(file_name, "w", encoding='utf-8') as out_file:
        print('Введите строки \nВведите пустую строку, чтобы закончить ввод')
        while True:
            input_string = input('> ')
            if input_string:
                out_file.write(input_string + '\n')
            else:
                break
    return file_name


if __name__ == '__main__':
    logging()
