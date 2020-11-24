# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle
from time import ctime, time


class TrafficLight:
    __color = {
        'Red': 7,
        'Yellow': 2,
        'Green': 2
    }

    def running(self):
        for key, value in cycle(self.__color.items()):
            print(f'{ctime(time())}: {key}')
            sleep(value)


if __name__ == '__main__':
    TrafficLight().running()
