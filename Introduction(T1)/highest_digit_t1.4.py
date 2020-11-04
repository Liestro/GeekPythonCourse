# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Получение данных от пользователя
input_number = int(input('input your number: '))

result = 0
while input_number > 0:
    # Крайняя правая цифра числа
    current_digit = input_number % 10

    # Исключение крайней правой цифры числа
    input_number = input_number // 10

    # Обновление максимальной цифры
    if current_digit > result:
        result = current_digit

print(result)
