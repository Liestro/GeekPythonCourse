# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a=0, b=0):
        self.coeffs = (a, b)

    @property
    def coeffs(self):
        return self.__coeffs

    @coeffs.setter
    def coeffs(self, coeffs):
        self.__coeffs = tuple([0, 0])

        try:
            self.__coeffs = tuple(map(float, coeffs))
        except ValueError as err:
            print(err)

    def __str__(self):
        return f'{self.coeffs[0]} + {self.coeffs[1]} * i'

    def __add__(self, other):
        return Complex(*list(map(sum, zip(self.coeffs, other.coeffs))))

    def __mul__(self, other):
        # (a + bi)(c + di) = ac - bd + (ad + bc)i
        a, b = self.coeffs
        c, d = other.coeffs
        return Complex(a * c - b * d, a * d + b * c)


if __name__ == '__main__':
    c1 = Complex(5, 9)
    c2 = Complex(-3, 7)
    print(c1 + c2)
    print(c1 * c2)
