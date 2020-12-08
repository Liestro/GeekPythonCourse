# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class NewZeroDivisionError(Exception):
    def __init__(self, txt='Zero Division'):
        self.txt = txt


if __name__ == '__main__':
    try:
        numerator, denominator = map(float, input('Введите числитель и знаменатель через пробел\n>').split())
        # Обычно сравнивание с нулем дробей заканчивается плохо, но в данном случае это, мне показалось,
        # позволительно т.к. анализируются данные, введенные пользователем
        if denominator == 0:
            raise NewZeroDivisionError('Знаменатель равен нулю')
    except ValueError:
        print('Необходимо ввести 2 числа')
    except NewZeroDivisionError as zderr:
        print(zderr)
    else:
        print(numerator / denominator)
