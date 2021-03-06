# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    # Значение удельной массы сразу установлено в тоннах
    __linear_density = 0.025
    __thick = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        return self._width * self._length * self.__thick * self.__linear_density


if __name__ == '__main__':
    print(Road(5000, 20).asphalt_mass())
