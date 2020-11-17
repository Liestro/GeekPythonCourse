# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(input_string):
    all_chars = 'qwertyuiopasdfghjklzxcvbnm'
    return not set(input_string).difference(all_chars) and input_string.title()


def main():
    inp_str = input('Введите строку из нескольких слов\n>').split()
    result_string = ''
    for i in inp_str:
        func_res = int_func(i)
        if func_res:
            result_string += f'{func_res} '

    print(result_string)


main()
