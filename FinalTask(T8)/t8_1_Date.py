# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class IncorrectDate(Exception):
    def __init__(self, txt='Incorrect Date'):
        self.txt = txt


class Date:
    days_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, date_string='01-01-1900'):
        self.date = date_string

    def __str__(self):
        return f'{self.date[0]:02}-{self.date[1]:02}-{self.date[2]:04}'

    @property
    def date(self):
        return [self.__dd, self.__mm, self.__yyyy]

    @date.setter
    def date(self, date_string):
        self.__dd, self.__mm, self.__yyyy = self.convert(date_string)

    @classmethod
    def convert(cls, date_string):
        try:
            res = list(map(int, date_string.split('-')))
            if not Date.is_date_valid(res):
                raise IncorrectDate('Date is out of range')
            return res
        except ValueError:
            raise IncorrectDate('Date must be numbers')

    @staticmethod
    def is_date_valid(date_list):
        if 1 <= date_list[1] <= 12 \
                and 1 <= date_list[2] < 9999 \
                and 1 <= date_list[0] <= Date.days_in_months[date_list[1]] \
                + int(not date_list[2] % 4 and date_list[1] == 2):
            return True
        return False


if __name__ == '__main__':
    try:
        date_lst = Date.convert('29-02-2024')
        print(date_lst)
        print(Date.is_date_valid(date_lst))
        date = Date('29-02-2025')
        print(date)
    except IncorrectDate as err:
        print(err)

