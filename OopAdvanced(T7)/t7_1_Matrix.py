# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка:
# сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, elements):
        self.elements = [[]]
        try:
            self.elements = [list(map(float, el)) for el in elements]
        except ValueError:
            print('Matrix can contain only numbers')

    def __str__(self):
        return '\n\n'.join([' '.join([f"{i:10}" for i in row]) for row in self.elements])

    def __add__(self, other):
        res = []
        for i in zip(self.elements, other.elements):
            sub_res = []
            for j in zip(i[0], i[1]):
                sub_res.append(sum(j))
            res.append(sub_res)
        return Matrix(res)


if __name__ == '__main__':
    matr = Matrix([[1.57, 2], [3, '8']])
    matr_2 = Matrix([[5, 6], [8, 9]])
    print(matr + matr_2)
