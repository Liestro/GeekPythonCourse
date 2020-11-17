# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    try:
        temp_list = [num_1, num_2, num_3]
        return sum(temp_list) - min(temp_list)
    except TypeError as err:
        return "from func my_func: Функция может работать тольо с числами"


print(my_func('l', -13, 1))
