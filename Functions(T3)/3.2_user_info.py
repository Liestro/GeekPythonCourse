# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, birthyear, city, email, phone):
    return f'Name: {name}, Surname: {surname}, Birthday: {birthyear}, City: {city}, e-mail: {email}, phone: {phone}'


print(user_info(name=input('Введите имя\n>'), surname=input('Введите фамилию\n>'),
                birthyear=input('Введите год рождения\n>'), city=input('Введите город проживания\n>'),
                email=input('Введите e-mail\n>'), phone=input('Введите номер телефона\n>')))
