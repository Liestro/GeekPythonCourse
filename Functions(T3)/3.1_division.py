# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(num_1, num_2):
    """
    Функция возвращает резульат деления num_1 на num_2

    :param num_1:
    :param num_2:
    :return Результат деления или ZeroDivisionError при делении на 0:

    """
    try:
        return num_1 / num_2
    except ZeroDivisionError as zero_err:
        return zero_err


try:
    # Получение данных от пользователя
    n1, n2 = input('Введите 2 числа через пробел\n>').split()
    print(divide(float(n1), float(n2)))

    # Обработка возможных исключений
except ValueError as val_err:
    print("Необходимо ввести 2 числа")
