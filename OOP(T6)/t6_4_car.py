# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: _speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        try:
            self._speed = int(speed)
        except ValueError:
            print("From class 'Car': Speed must be an integer")
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is moving')

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f"{self.name}'s Speed: {self._speed}")
        
        
class TownCar(Car):
    def show_speed(self):
        super(TownCar, self).show_speed()
        if self._speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self._speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name, True)


if __name__ == '__main__':
    sc = SportCar(150, 'Red', 'Audi', False)
    tc = TownCar(70, 'Blue', 'Suzuki', False)
    wc = WorkCar(40, 'Yellow', 'Honda')
    pc = PoliceCar(100500, 'Blue', 'BMW')

    for car in [sc, tc, wc, pc]:
        print(car.color, car.name, car.is_police)
        car.go()
        car.turn('Left')
        car.show_speed()
        car.stop()
        print('-' * 100)
