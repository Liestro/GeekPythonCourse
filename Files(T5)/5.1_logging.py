# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

def logging():
    with open("log.txt", "w", encoding='utf-8') as out_file:
        input_string = None
        while input_string != '':
            input_string = input('> ')
            out_file.write(input_string + '\n')


if __name__ == '__main__':
    logging()
