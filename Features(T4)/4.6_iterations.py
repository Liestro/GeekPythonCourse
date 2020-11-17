# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import cycle, count
from random import randint

# Генерируем список для iter_cycle
start_list = [randint(10, 101) for i in range(10)]
print(start_list)

# Создаем итераторы
iter_count = count(0)
iter_cycle = cycle(start_list)

# Выводим результат
for i in range(len(start_list) * 2):
    print(iter_count.__next__(), iter_cycle.__next__())
