# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к
# клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке
# https://pythonworld.ru/osnovy/peregruzka-operatorov.html.

class Cell:
    def __init__(self, number=0):
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = 0

        try:
            number = int(number)
        except ValueError:
            print("Количество клеток может быть только целым числом")

        if number < 0:
            self.__number = 0
        else:
            self.__number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        # Там в сеттере все, что меньше нуля, в ноль обращается
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, n_in_row):
        return '\n'.join(['*' * n_in_row for _ in range(self.number // n_in_row)]) + '\n' + \
               '*' * (self.number % n_in_row)


if __name__ == '__main__':
    c = Cell(7)
    c2 = Cell(5)
    print(c.number)
    print(c + c2)
    print(c - c2)
    print(c * c2)
    print(c // c2)
    print((c + c2).make_order(6))
