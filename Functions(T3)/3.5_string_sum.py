# 5. Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def main():
    big_sum = 0
    is_q_here = False
    while not is_q_here:
        input_string = input('Введите строку числе через пробел или "Q" для выхода\n>').split()

        is_q_here = input_string.count('Q') != 0
        if is_q_here:
            input_string = input_string[:input_string.index('Q')]

        try:
            little_sum = sum(map(int, input_string))
            big_sum += little_sum
            print(f'{little_sum}({big_sum})')
        except ValueError as err:
            print(err)
    else:
        print('Exit')


main()
