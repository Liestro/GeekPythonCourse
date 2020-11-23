# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title='Blue'):
        self._title = title

    def draw(self):
        print(f'Запуск отрисовки. Цвет - {self._title}')


class Pen(Stationery):
    def draw(self):
        print('Pen: ')
        super(Pen, self).draw()


class Pencil(Stationery):
    def draw(self):
        print('Pencil: ')
        super(Pencil, self).draw()


class Handle(Stationery):
    def draw(self):
        print('Handle: ')
        super(Handle, self).draw()


if __name__ == '__main__':
    for i in [Pencil(), Pen("Red"), Handle()]:
        i.draw()
        print('-' * 100)
