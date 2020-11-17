# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

# Генерация четных
evens = [i for i in range(100, 1001) if i % 2 == 0]
print(evens)


def innovative_product(num_1, num_2):
    """
    Фунцкия восзвращает результат произведения аргументов

    :param num_1: Первый аргумент
    :param num_2: Второй аргумент
    :return: Результат умножения
    """

    return num_1 * num_2


# Вычисляем результирующее значение
result_list = reduce(innovative_product, evens)
print(result_list)