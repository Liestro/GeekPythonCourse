# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Создание контейнеров с соответствием номеров и месяцев
list_months = [
    "Зима",
    "Зима",
    "Весна",
    "Весна",
    "Весна",
    "Лето",
    "Лето",
    "Лето",
    "Осень",
    "Осень",
    "Осень",
    "Зима"
]

dict_months = {
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима"
}

dict_list_months = {
    "Зима": [1, 2, 3],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8],
    "Осень": [9, 10, 11]
}

# Получение данных от пользователя
n_month = input('Введите номер месяца:\n> ')

if not (n_month.isdigit() and 1 <= int(n_month) <= 12):
    # Проверка введенных данных на корректность
    print('Номер месяца должен быть целым числом в диапазоне [1, 12]')
else:
    # Вычисление результата
    n_month = int(n_month)
    print(f'{n_month}-й месяц из списка это {list_months[n_month - 1]}')
    print(f'{n_month}-й месяц из словаря это {dict_months[n_month]}')
    for key, val in dict_list_months.items():
        if val.count(n_month) == 1:
            print(f'{n_month}-й месяц из словаря со списками это {key}')

