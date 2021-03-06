# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint

# Генерируем исходный список
start_list = [randint(0, 99) for i in range(20)]  # [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(start_list)

# Генерируем результирующий список
result_list = [start_list[i] for i in range(1, len(start_list)) if start_list[i] > start_list[i - 1]]
print(result_list)
