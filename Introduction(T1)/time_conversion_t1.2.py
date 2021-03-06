# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Получение секунд от пользователя
# Здесь мы отбрасываем все, что после запятой: нам это неинтересно
all_secs = int(input('Input time in seconds: '))

# Проверка на отрицательное количество секунд
# Python обрабатывает отрицательные числа не так как нужно,
# а закономерность там какая-то непростая.
is_negative = all_secs < 0
all_secs = abs(all_secs)

# Расчет значений часов, минут и секунд
hours = all_secs // 3600
minutes = (all_secs % 3600) // 60
seconds = all_secs % 60

# Вывод данных в нужном формате.
# Так же выводится минус, если пользователь ввел отрицательное кол-во секунд
if is_negative:
    print('-', end='')
print(f'{hours:02}:{minutes:02}:{seconds:02}')
