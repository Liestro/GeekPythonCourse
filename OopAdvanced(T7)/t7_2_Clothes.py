# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __add__(self, other):
        return round(self.cloth() + other.cloth(), 2)

    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        self.__size = 0

        try:
            size = float(size)
        except ValueError:
            print('Размером может быть только число')
            return

        if size > 70:
            self.__size = 70
        elif size < 0:
            self.__size = 0
        else:
            self.__size = size

    def cloth(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = 0

        try:
            height = float(height)
        except ValueError:
            print("Ростом может быть только число")
            return

        if height > 220:
            self.__height = 220
        elif height < 120:
            self.__height = 120
        else:
            self.__height = height

    def cloth(self):
        return round(2 * self.__height + 0.3, 2)


if __name__ == '__main__':
    c = Coat('55')
    print(c.size)

    s = Suit("10")
    print(s.height)

    print(c + s)
