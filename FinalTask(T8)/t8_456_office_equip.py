# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod


class NotEquipmentError(Exception):
    def __init__(self, txt='Not Equipment'):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self.__equip_list = []

    def __str__(self):
        return f'In Warehouse: \n' + '\n'.join(list(map(str, self.equip_list)))

    @property
    # Это передача оргтехники
    def equip_list(self):
        return self.__equip_list

    @equip_list.setter
    # Это прием техники
    def equip_list(self, eqlst):
        for el in eqlst:
            self.equip_list_append(el)

    def equip_list_append(self, eq):
        if type(eq) != Printer and type(eq) != Scanner and type(eq) != Copier:
            raise NotEquipmentError("We can collect only Equipment")
        self.__equip_list.append(eq)


class Equipment(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        try:
            self.__price = float(price)
        except ValueError:
            raise ValueError('Price can be only float')

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        try:
            self.__quantity = int(quantity)
        except ValueError:
            raise ValueError('Quantity can be only int')


class Printer(Equipment):
    def __str__(self):
        return f'Printer: Name - {self.name}, Price - {self.price}, Quantity - {self.quantity}'


class Scanner(Equipment):
    def __str__(self):
        return f'Scanner: Name - {self.name}, Price - {self.price}, Quantity - {self.quantity}'


class Copier(Equipment):
    def __str__(self):
        return f'Copier: Name - {self.name}, Price - {self.price}, Quantity - {self.quantity}'


if __name__ == '__main__':
    mode = None
    wr = Warehouse()
    while mode != 'q':
        print()
        try:
            mode = input('Выберите действие:\n'
                         ' i - поместить технику на склад\n'
                         ' p - показать имеющиюся на складе технику\n'
                         ' q - выход\n> ')
            if mode == 'q':
                continue
            if mode == 'p':
                print(wr)
                continue
            if mode != 'i':
                print('Unknown command')
                continue

            eq_type = input('Выберите тип товара:\n'
                            ' 1 - Принтер'
                            ' 2 - Сканер'
                            ' 3 - Ксерокс\n> ')
            eq_type = int(eq_type)

            if eq_type == 1:
                eq_name = input('Введите имя товара\n> ')
                eq_price = input('Введите цену товара\n> ')
                eq_quantity = input('Введите количество товара\n> ')
                wr.equip_list_append((Printer(eq_name, eq_price, eq_quantity)))
                print(f'Вы добавили товар. Текущее состояние склада:\n {wr}')
            elif eq_type == 2:
                eq_name = input('Введите имя товара\n> ')
                eq_price = input('Введите цену товара\n> ')
                eq_quantity = input('Введите количество товара\n> ')
                wr.equip_list_append((Scanner(eq_name, eq_price, eq_quantity)))
                print(f'Вы добавили товар. Текущее состояние склада:\n {wr}')
            elif eq_type == 3:
                eq_name = input('Введите имя товара\n> ')
                eq_price = input('Введите цену товара\n> ')
                eq_quantity = input('Введите количество товара\n> ')
                wr.equip_list_append((Scanner(eq_name, eq_price, eq_quantity)))
                print(f'Вы добавили товар. Текущее состояние склада:\n {wr}')
            else:
                wr.equip_list_append('Something Unknown')
        except ValueError as err:
            print(err)
        except NotEquipmentError as err:
            print(err)
